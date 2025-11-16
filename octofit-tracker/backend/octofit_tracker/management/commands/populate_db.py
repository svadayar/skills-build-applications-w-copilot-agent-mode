from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel, is_superhero=True)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel, is_superhero=True)
        hulk = User.objects.create(email='hulk@marvel.com', name='Hulk', team=marvel, is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc, is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc, is_superhero=True)
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc, is_superhero=True)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body strength', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        yoga = Workout.objects.create(name='Yoga', description='Flexibility', difficulty='Easy')

        # Create Activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=spiderman, type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user=hulk, type='Yoga', duration=15, date=timezone.now().date())
        Activity.objects.create(user=batman, type='Running', duration=40, date=timezone.now().date())
        Activity.objects.create(user=superman, type='Pushups', duration=25, date=timezone.now().date())
        Activity.objects.create(user=wonderwoman, type='Yoga', duration=35, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=spiderman, score=90)
        Leaderboard.objects.create(user=hulk, score=80)
        Leaderboard.objects.create(user=batman, score=110)
        Leaderboard.objects.create(user=superman, score=120)
        Leaderboard.objects.create(user=wonderwoman, score=115)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
