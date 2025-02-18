from app import create_app
from models import db, User, Folder, Record, Mistake
from datetime import datetime

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Пример добавления тестовых данных
    user = User(
        first_name="John",
        last_name="Doe",
        login="john_doe",
        password_hash="hashed_pass",
        teacher=0
    )
    db.session.add(user)
    db.session.commit()

    folder = Folder(name="My Folder", user_id=user.id)
    db.session.add(folder)
    db.session.commit()

    record = Record(
        user_id=user.id,
        trash=0,
        length=120.5,
        audio_file="path/to/audio.mp3",
        datetime=datetime.utcnow()
    )
    db.session.add(record)
    db.session.commit()

    mistake = Mistake(
        record_id=record.id,
        comment="Wrong pronunciation",
        time_of_mistake=10.5,
        type=1
    )
    db.session.add(mistake)
    db.session.commit()

    print("Database created and populated with test data.")
