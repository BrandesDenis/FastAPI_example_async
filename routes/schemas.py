from pydantic import BaseModel


class NoteIn(BaseModel):
    text: str
    completed: bool
    # field2: str


class Note(BaseModel):
    id: int
    text: str
    completed: bool
    # field2: str
