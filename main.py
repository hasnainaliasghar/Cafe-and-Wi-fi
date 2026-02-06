from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer, String, Float, Column

class BaseModel(DeclarativeBase):
    pass

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'


db = SQLAlchemy(model_class=BaseModel)
db.init_app(app)

class Cafes(db.Model):
    __tablename__ = 'cafe'
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String, unique=True,nullable=False)
    map_url : Mapped[str] = mapped_column(String, nullable=False)
    img_url : Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    has_sockets: Mapped[int] = mapped_column(Integer, nullable=False)
    has_toilet: Mapped[int] = mapped_column(Integer, nullable=False)
    has_wifi: Mapped[int] = mapped_column(Integer, nullable=False)
    can_take_calls: Mapped[str] = mapped_column(String, nullable=False)
    seats: Mapped[str] = mapped_column(String, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String, nullable=False)



@app.route('/')
def home():
    cafes = db.session.query(Cafes).all()
    print(cafes)
    return render_template('index.html',cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
