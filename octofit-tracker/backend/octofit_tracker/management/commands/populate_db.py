from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Workout, Activity, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel),
            User.objects.create(email='captain@marvel.com', username='Captain America', team=marvel),
            User.objects.create(email='batman@dc.com', username='Batman', team=dc),
            User.objects.create(email='superman@dc.com', username='Superman', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Upper body workout', difficulty='Easy'),
            Workout.objects.create(name='Running', description='Cardio workout', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], workout=workouts[0], duration_minutes=30, calories_burned=200)
        Activity.objects.create(user=users[1], workout=workouts[1], duration_minutes=45, calories_burned=400)
        Activity.objects.create(user=users[2], workout=workouts[0], duration_minutes=20, calories_burned=150)
        Activity.objects.create(user=users[3], workout=workouts[1], duration_minutes=60, calories_burned=500)

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=600, rank=1)
        Leaderboard.objects.create(team=dc, total_points=650, rank=2)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
