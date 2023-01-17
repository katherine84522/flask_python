from app import app
from models import db, User




def run_seeds():
    print('Seeding database ... 🌱')
    with app.app_context():
        user1 = User('Catherine', 'k13@gmail.com', '1111')
        db.session.add([user1])
        db.session.commit()
        print('Done! 🌳')

        
