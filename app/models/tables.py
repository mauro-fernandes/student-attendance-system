from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
    
    def __repr__(self):
        return '<User %r>' % self.username
    

    
class Attendance(db.Model):
    __tablename__ = 'attendances'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    


    
class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', foreign_keys=user_id)
    
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
        
    def __repr__(self):
        return '<Post %r>' % self.id

      
class Follow(db.Model):
    __tablename__ = 'follows'
    
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    follower = db.relationship('User', foreign_keys=follower_id)
    followed = db.relationship('User', foreign_keys=followed_id)
    
    def __init__(self, follower_id, followed_id):
        self.follower_id = follower_id
        self.followed_id = followed_id
        
    def __repr__(self):
        return '<Follow %r>' % self.id
    
    
class Like(db.Model):
    __tablename__ = 'likes'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    post = db.relationship('Post', foreign_keys=post_id)
    user = db.relationship('User', foreign_keys=user_id)
    
    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id
        
    def __repr__(self):
        return '<Like %r>' % self.id
    
class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    post = db.relationship('Post', foreign_keys=post_id)
    user = db.relationship('User', foreign_keys=user_id)
    
    def __init__(self, content, post_id, user_id):
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
        
    def __repr__(self):
        return '<Comment %r>' % self.id
    
class Timeline(db.Model):
    __tablename__ = 'timelines'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    post = db.relationship('Post', foreign_keys=post_id)
    user = db.relationship('User', foreign_keys=user_id)
    
    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id
        
    def __repr__(self):
        return '<Timeline %r>' % self.id
    
class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', foreign_keys=user_id)
    
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
        
    def __repr__(self):
        return '<Notification %r>' % self.id
    
class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', foreign_keys=user_id)
    
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
        
    def __repr__(self):
        return '<Message %r>' % self.id
 
    
    
db.create_all()