from ext import app, db
from models import Product, User




with app.app_context():
    db.create_all()

    admin_user = User("admin1", "lashakvitsiani5@gmail.com", "adminpassword123", "admin")
    db.session.add(admin_user)
    db.session.commit()
