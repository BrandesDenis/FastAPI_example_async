from schemas import NoteIn
from database import database
from models import notes


async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


async def create_note(note: NoteIn):
    query = notes.insert().values(
        text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}
