from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pikachu_game.db'
app.config['SECRET_KEY'] = 'secretkey123'
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)

# Cấu trúc model cho User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, default=0)  # Điểm mặc định là 0

    def __repr__(self):
        return f"User('{self.fullname}', '{self.email}', '{self.score}')"

# Route chính cho trang đăng ký
@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        
        # Tạo người dùng mới với điểm mặc định là 0
        new_user = User(fullname=fullname, email=email, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            session.rollback()
            print("Email đã tồn tại!")
        
        flash('Đăng ký thành công!', 'success')
        return redirect(url_for('leaderboard'))
    
    return render_template('signup.html')


# Route đăng nhập
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    user = User.query.filter_by(email=email).first()  # Tìm người dùng theo email
    if user and check_password_hash(user.password, password):  # Kiểm tra mật khẩu
        flash('Đăng nhập thành công!', 'success')
        return redirect(url_for('dashboard'))  # Redirect đến trang dashboard
    else:
        flash('Email hoặc mật khẩu không đúng!', 'danger')
        return redirect(url_for('login'))

# Route chính cho trang chủ game
@app.route('/index')
def index():
    return render_template('index.html')

# Route cập nhật điểm game
@app.route('/update_score', methods=['POST'])
def update_score():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    score = request.form['score']
    
    user = User.query.get(user_id)
    user.score = score
    db.session.commit()
    
    flash('Điểm của bạn đã được cập nhật!', 'success')
    return redirect(url_for('leaderboard'))

# Route hiển thị bảng xếp hạng
@app.route('/leaderboard')
def leaderboard():
    users = User.query.order_by(User.score.desc()).all()
    return render_template('leaderboard.html', users=users)

# Chạy ứng dụng
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Tạo tất cả bảng nếu chưa có
    app.run(debug=True)
