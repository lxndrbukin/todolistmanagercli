import sqlite3
from pydantic import BaseModel, Field, computed_field
from datetime import datetime, timezone
from enum import Enum

DB_PATH = "tasks.db"

db_table = '''
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        entry TEXT NOT NULL,
        priority TEXT NOT NULL,
        due DATETIME,
        completed BOOLEAN,
        completed_at DATETIME
    )
'''

class Priority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Task(BaseModel):
    id: int
    entry: str
    priority: Priority = Field(default="medium")
    due: datetime
    completed: bool = False
    completed_at: datetime | None = Field(examples=[None])
    @computed_field
    def is_overdue(self) -> bool:
        return self.due < datetime.now(timezone.utc) and self.completed_at is None


class Database:
	def __init__(self, db_path=DB_PATH):
		self._db_path = db_path

	@property
	def db_path(self):
		return self._db_path

	def init_db(self):
		with sqlite3.connect(self.db_path) as conn:
			conn.execute(db_table)
			conn.commit()

	def load_db():
		conn = sqlite3.connect(DB_PATH)
		conn.row_factory = sqlite3.Row
		try:
			yield conn
		finally:
			conn.close()

	def row_to_task(row: tuple) -> Task:
		return Task(
			id=row[0],
			entry=row[1],
			priority=Priority(row[2]),
			due=datetime.fromisoformat(row[3]),
			completed=bool(row[4]),
			completed_at=datetime.fromisoformat(row[5]) if row[5] else None
		)
	
	def read_entries(self):
		return []