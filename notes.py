from flask import make_response, abort
from config import db
from models import Person, Note, NoteSchema

def read_all():
    """
    This function responds to a request for /api/people/notes
    with the complete list of notes, sorted by note timestamp
    :return:                json list of all notes for all people
    """
    # Query the database for all the notes
    notes = Note.query.order_by(db.desc(Note.timestamp)).all()

    # Serialize the list of notes from our data
    note_schema = NoteSchema(many=True, exclude=["person.notes"])
    data = note_schema.dump(notes)
    return data
    pass

def read_one(person_id, note_id):
    """
    This function responds to a request for
    /api/people/{person_id}/notes/{note_id}
    with one matching note for the associated person

    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    # Query the database for the note
    note = (
        Note.query.join(Person, Person.person_id == Note.person_id)
        .filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    # Was a note found?
    if note is not None:
        note_schema = NoteSchema()
        data = note_schema.dump(note)
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {note_id}")

def update(person_id, noteid):
    pass

def create(person_id, note_id):
    pass

def delete(person_id, note_id):
    pass
