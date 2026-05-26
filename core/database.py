import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


class DatabaseManager:

    def __init__(self):

        self.connection = psycopg2.connect(DATABASE_URL)
        self.cursor = self.connection.cursor()

        print("[Database] PostgreSQL Connected Successfully")

    def save_task(self, task, decision, department):

        query = """
        INSERT INTO tasks (task, decision, department, status)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            task,
            decision,
            department,
            "completed"
        )

        self.cursor.execute(query, values)
        self.connection.commit()

        print("[Database] Task Saved")

    def save_memory(self, agent, message):

        query = """
        INSERT INTO memory (agent, message)
        VALUES (%s, %s)
        """

        values = (
            agent,
            message
        )

        self.cursor.execute(query, values)
        self.connection.commit()

        print("[Database] Memory Saved")

    def save_log(self, system_name, event):

        query = """
        INSERT INTO logs (system_name, event)
        VALUES (%s, %s)
        """

        values = (
            system_name,
            event
        )

        self.cursor.execute(query, values)
        self.connection.commit()

        print("[Database] Log Saved")