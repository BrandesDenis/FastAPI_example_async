from typing import List

from fastapi import APIRouter

from schemas import Note, NoteIn
from models import notes
import crud


router = APIRouter()


@router.get("/", response_model=List[Note])
async def read_notes():
    return await crud.read_notes()


@router.post("/", response_model=Note)
async def create_note(note: NoteIn):
    return await crud.create_note(note)
