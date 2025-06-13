from sqlalchemy.orm import Session
import model, schemas


# Generic CRUD 

def create_entity(db: Session, entity_model, entity_schema):
    db_entity = entity_model(**entity_schema.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def get_entity(db: Session, entity_model, entity_id: int):
    return db.query(entity_model).filter(entity_model.id == entity_id).first()


def get_all_entities(db: Session, entity_model):
    return db.query(entity_model).all()


def update_entity(db: Session, entity_model, entity_id: int, updated_schema):
    db_entity = get_entity(db, entity_model, entity_id)
    if not db_entity:
        return None
    for field, value in updated_schema.dict().items():
        setattr(db_entity, field, value)
    db.commit()
    db.refresh(db_entity)
    return db_entity


def delete_entity(db: Session, entity_model, entity_id: int):
    db_entity = get_entity(db, entity_model, entity_id)
    if db_entity:
        db.delete(db_entity)
        db.commit()
    return db_entity


# shortcuts
def create_play(db: Session, play: schemas.PlayCreate):
    return create_entity(db, model.Play, play)


def get_play(db: Session, play_id: int):
    return get_entity(db, model.Play, play_id)


def get_all_plays(db: Session):
    return get_all_entities(db, model.Play)


def update_play(db: Session, play_id: int, updated_play: schemas.PlayCreate):
    return update_entity(db, model.Play, play_id, updated_play)


def delete_play(db: Session, play_id: int):
    return delete_entity(db, model.Play, play_id)
