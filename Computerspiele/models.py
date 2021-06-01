from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Computerspiel(models.Model):

    name = models.CharField(max_length=100)
    beschreibung = models.TextField(max_length=500,
                                    blank=False
                                    )
    GENRE = [
        ('FPS', 'First-Person Shooter'),
        ('RPG', 'Role-Playing Game'),
        ('FG', 'Fighting Game'),
        ('RG', 'Racing Game'),
        ('SIM', 'Simulation'),
        ('TD', 'Tower Defense')
    ]

    FSK = [
        ('0', 'ab 0'),
        ('6', 'ab 6'),
        ('12', 'ab 12'),
        ('16', 'ab 16'),
        ('18', 'ab 18')
    ]

    developer_studio = models.CharField(max_length=100)
    # pages = models.IntegerField()  # Must call function to take effect
    date_released = models.DateTimeField(blank=True,
                                         default=date.today,
                                        )
    genre = models.CharField(max_length=10,
                             choices=GENRE,
                            )
    fsk = models.CharField(max_length=10,
                           choices=FSK,
                          default='0')
    ersteller = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    class Meta:
        ordering = ['name', '-genre']
        verbose_name = 'Computerspiel'
        verbose_name_plural = 'Computerspiele'

    def get_full_title(self):
        #return_string = self.name
        #if self.beschreibung:  # if beschreibung is not empty
        #    return_string = self.name + '\n Beschreibung: ' + self.beschreibung
        #return return_string
        return self.name + '\n Beschreibung: ' + self.beschreibung

    def __str__(self):
        return self.name + ' (' + self.genre + ')'

    def __repr__(self):
        return self.get_full_title() + ' / ' + self.developer_studio + ' / ' + self.genre