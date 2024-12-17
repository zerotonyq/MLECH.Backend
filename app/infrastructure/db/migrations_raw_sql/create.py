import asyncio
import os, sys

from sqlalchemy import text

from app.infrastructure.db.database import async_session


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.append(PROJECT_ROOT)

sql_file_path = 'create.sql'


async def create():
    async with async_session() as session:
        async with session.begin():
            try:
                with open(sql_file_path, 'r') as file:
                    sql_script = file.read()

                sql_commands = sql_script.split(';')

                for command in sql_commands:
                    command = command.strip()

                    if command:
                        await session.execute(text(command))

                    print("Tables successfully created")
            except Exception as error:
                 print(f"Error creating Tables: {error}")


if __name__ == "__main__":
    asyncio.run(create())