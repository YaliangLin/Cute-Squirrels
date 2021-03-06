from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class biaoge(models.Model):
    xx = models.FloatField (
        help_text = ('Latitude'),
        null = True,
    )

    yy = models.FloatField (
        help_text = ('Longtitude'),
        null = True,
    )

    Unique_Squirrel_ID = models.CharField(
        help_text = ('Unique Squirrel ID'),
        max_length = 50,
        unique = True,
        primary_key=True,
    )

    PM = 'PM'
    AM = 'AM'

    SHIFT_CHOICES = (
        (PM,'PM'),
        (AM,'AM'),
    )
    shift = models.CharField(
        default='',
        help_text = ('shift'),
        max_length = 50,
        choices = SHIFT_CHOICES,
        null = True,
    )

    date = models.DateField(
        default='1111-11-11',
        help_text = ('date'),
        null = True,
    )

    
    ADULT='Adult'
    JUVENILE='Juvenile'
    AGE_CHOICES = (
        (ADULT,'Adult'),
        (JUVENILE,'Juvenile'),
    )

    age = models.CharField(
        help_text = ('Age'),
        max_length = 50,
        choices = AGE_CHOICES,
        null = True,
    )


    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    FUR_COLOR_CHOICES = (
        (GRAY,'Gray'),
        (CINNAMON,'Cinnamon'),
        (BLACK,'Black'),
    )

    primary_fur_color = models.CharField(
        help_text = ('Primary Fur Color'),
        max_length = 50,
        choices = FUR_COLOR_CHOICES,
        null = True,
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = (
        (GROUND_PLANE,'Ground Plane'),
        (ABOVE_GROUND,'Above Ground'),
    )

    location = models.CharField(
        help_text = ('Location'),
        max_length = 50,
        choices = LOCATION_CHOICES,
        null = True,
    )

    specific_location = models.CharField(
        help_text = ('Specific Location'),
        max_length = 50,
        null = True,
    )

    running = models.BooleanField(
        help_text = ('Running?'),
        default = False,
    )

    chasing = models.BooleanField(
        help_text = ('Chasing?'),
        default = False,
    )

    climbing = models.BooleanField(
        help_text = ('Climbing?'),
        default = False,
    )

    eating = models.BooleanField(
        help_text = ('Eating?'),
        default = False,
    )

    foraging = models.BooleanField(
        help_text = ('Foraging?'),
        default = False,
    )

    other_activities = models.CharField(
        help_text = ('Other Activities'),
        max_length = 50,
        default = '',
        null = True,
    )

    kuks = models.BooleanField(
        help_text = ('Kuks?'),
        default = False,
    )

    quaas = models.BooleanField(
        help_text = ('Quaas?'),
        default = False,
    )

    tail_flags = models.BooleanField(
        help_text = ('Tail Flags?'),
        default = False,
    )

    tail_twitches = models.BooleanField(
        help_text = ('Tail Twitches?'),
        default = False,
    )

    approaches = models.BooleanField(
        help_text = ('Approaches?'),
        default = False,
    )

    indifferent = models.BooleanField(
        help_text = ('Indifferent?'),
        default = False,
    )

    runs_from = models.BooleanField(
        help_text = ('Runs From?'),
        default = False,)
        
    moans = models.BooleanField(
        help_text= ('Moans'),
        default = False,)
    
    profile_image = models.ImageField(
        help_text= ('Profile picture of pet'),
        upload_to = "img/",
        null = True,
    )

    have_image = models.BooleanField(
        help_text=('if this squirrel has image, please check it on'),
        default = False,
    )
    
    def __str__(self):
        return self.Unique_Squirrel_ID