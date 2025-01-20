from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

@app.before_request
def create_tables():
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User({self.name}, {self.email})"

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, help='Name of the user', required=True)
user_args.add_argument('email', type=str, help='Email of the user', required=True)

userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False) # minutes
    calories = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Workout({self.type}, {self.duration} minutes, {self.calories} calories)"
    
workout_args = reqparse.RequestParser()
workout_args.add_argument('user_id', type=int, help='User ID', required=True)
workout_args.add_argument('type', type=str, help='Type of workout (e.g. running)', required=True)
workout_args.add_argument('duration', type=int, help='Duration of workout in minutes', required=True)
workout_args.add_argument('calories', type=int, help='Calories burned', required=True)

workoutFields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'type': fields.String,
    'duration': fields.Integer,
    'calories': fields.Integer
}


class Users(Resource):
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = User(name=args['name'], email=args['email'])
        existing_user = User.query.filter_by(email=args['email']).first()
        if existing_user:
            abort(400, message="A user with this email already exists.")

        db.session.add(user)
        db.session.commit()
        return user, 201

class UserById(Resource):
    @marshal_with(userFields)
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message='User not found')
        return user
    
    @marshal_with(userFields)
    def patch(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message='User not found')
        args = user_args.parse_args()
        user.name = args['name']
        user.email = args['email']
        db.session.commit()
        return user

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message='User not found')
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}, 204
    

class WorkoutResource(Resource):
    @marshal_with(workoutFields)
    def get(self, workout_id):
        workout = Workout.query.filter_by(id=workout_id).first()
        if not workout:
            abort(404, message="Workout not found")
        return workout

    @marshal_with(workoutFields)
    def post(self):
        args = workout_args.parse_args()
        workout = Workout(user_id=args['user_id'], type=args['type'], duration=args['duration'], calories=args['calories'])
        db.session.add(workout)
        db.session.commit()
        return workout, 201

    @marshal_with(workoutFields)
    def patch(self, workout_id):
        workout = Workout.query.filter_by(id=workout_id).first()
        if not workout:
            abort(404, message="Workout not found")
        args = workout_args.parse_args()
        workout.user_id = args['user_id']
        workout.type = args['type']
        workout.duration = args['duration']
        workout.calories = args['calories']
        db.session.commit()
        return workout
    
    def delete(self, workout_id):
        workout = Workout.query.filter_by(id=workout_id).first()
        if not workout:
            abort(404, message="Workout not found")
        db.session.delete(workout)
        db.session.commit()
        return {'message': 'Workout deleted'}, 204

class UserWorkouts(Resource):
    @marshal_with(workoutFields)
    def get(self, user_id):
        workouts = Workout.query.filter_by(user_id=user_id).all()
        return workouts

api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:user_id>')
api.add_resource(UserWorkouts, '/users/<int:user_id>/workouts')
api.add_resource(WorkoutResource, '/workouts', '/api/workouts/<int:workout_id>')


@app.route('/')
def home():
    return

if __name__ == '__main__':
    app.run(debug=True)