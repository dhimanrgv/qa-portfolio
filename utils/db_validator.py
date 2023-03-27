"""
utils/db_validator.py
Database validation helper for backend/API testing.
Uses sqlite3 (stdlib) for portability. Replace with psycopg2/mysql-connector in real projects.
"""
import sqlite3
from contextlib import contextmanager
from framework.logger import get_logger

logger = get_logger(__name__)


class DBValidator:
    def __init__(self, db_path=":memory:"):
        self.db_path    = db_path
        self.connection = None
        self.cursor     = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection: self.connection.close()

    def execute_query(self, sql, params=()):
        logger.debug(f"SQL: {sql} | params: {params}")
        self.cursor.execute(sql, params)
        return [dict(r) for r in self.cursor.fetchall()]

    def execute_single(self, sql, params=()):
        results = self.execute_query(sql, params)
        return results[0] if results else None

    def get_row_count(self, table, condition="", params=()):
        where = f"WHERE {condition}" if condition else ""
        r = self.execute_single(f"SELECT COUNT(*) AS cnt FROM {table} {where}", params)
        return r["cnt"] if r else 0

    def assert_record_exists(self, table, condition, params=()):
        count = self.get_row_count(table, condition, params)
        assert count > 0, f"Expected record in {table!r} WHERE {condition}"

    def assert_record_count(self, table, expected, condition="", params=()):
        actual = self.get_row_count(table, condition, params)
        assert actual == expected, f"Expected {expected} rows, got {actual}"

    def assert_column_value(self, table, column, expected, condition, params=()):
        row = self.execute_single(f"SELECT {column} FROM {table} WHERE {condition}", params)
        assert row and row[column] == expected,             f"Column {column!r}: expected {expected!r}, got {row.get(column) if row else None!r}"

    def __enter__(self): self.connect(); return self
    def __exit__(self, *args): self.disconnect()
