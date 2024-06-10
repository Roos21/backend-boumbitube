from django.db import models
from django.urls import reverse
from hashid_field import HashidAutoField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission

from accounts.managers import CustomUserManager
from musics.models import StyleMusical

# Create your models here.

class TimeStamps(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateField(auto_now_add=True, null=True, blank=True)
    class Meta:
        abstract = True
class User(AbstractBaseUser, PermissionsMixin, TimeStamps):
    
    reference_id = HashidAutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subscriptionDate = models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, related_name='btube_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='btube_users_permissions', blank=True)

    is_cancel = models.BooleanField(default=False)
    is_first_connexion = models.BooleanField(default=True)
    is_activated = models.BooleanField(default=False, blank=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    
    def get_full_name(self):
        return f"{self.firstName} {self.lastName}"
    
    def get_absolute_url(self):
        return reverse("user_manager:profil", kwargs={"pk": self.reference_id})
    
class Subscriber(TimeStamps):
    
    reference_id = HashidAutoField(primary_key=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)
    civilStatus = models.CharField(max_length=255)
    dateOfBirth = models.DateField(default=timezone.now)
    phoneNumber = models.CharField(max_length=20)
    subscriptionDate = models.DateField(default=timezone.now)
    isPremiumSubscriber = models.BooleanField(default=False)
    # watchHistory = models.ManyToManyField('Video', related_name='watched_by_subscriber')
    # favorites = models.ManyToManyField('Music', related_name='favorited_by_subscriber')

    facebook = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    tiktok = models.URLField(max_length=255, blank=True, null=True)
    youtube = models.URLField(max_length=255, blank=True, null=True)
    
    # token = models.OneToOneField(Token, on_delete=models.CASCADE)
    # paymentInfo = models.OneToOneField(PaymentInfo, on_delete=models.CASCADE, null=True, blank=True)
    
    subscription_date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.alias}'  
    

    @property
    def get_facebook_link(self):
        return self.facebook if self.facebook else ''

    @property
    def get_instagram_link(self):
        return self.instagram if self.instagram else ''

    @property
    def get_tiktok_link(self):
        return self.tiktok if self.tiktok else ''

    @property
    def get_youtube_link(self):
        return self.youtube if self.youtube else ''
    
    def __str__(self):
        return self.alias 
    
    def get_id(self):
        
        return f'{self.alias}'
    
    
class Artist(TimeStamps):
    
    reference_id = HashidAutoField(primary_key=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank=True)
    alias = models.CharField(max_length=255)
    civilStatus = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    phoneNumber = models.CharField(max_length=20)
    firstHitSingle = models.CharField(max_length=255, null=True, blank=True)
    isPremiem = models.BooleanField(default=True)
    # Modification des champs de médias sociaux
    facebook = models.URLField(max_length=255, null = True, blank=True)
    instagram = models.URLField(max_length=255, null = True, blank=True)
    tiktok = models.URLField(max_length=255, null = True, blank=True)
    youtube = models.URLField(max_length=255, null = True, blank=True)
    
    profileImage = models.ImageField(upload_to='images/artist/profile')
    coverImage = models.ImageField(upload_to='images/artist/cover')
    
    totalViews = models.IntegerField(null=True, blank=True)  # Nombre total de vues
    totalSubscribers = models.IntegerField(null=True, blank=True)  # Nombre total d'abonnés
    
    styleMusic = models.ManyToManyField(StyleMusical, blank=True)
    followers = models.ManyToManyField('Subscriber', related_name='followers', blank=True)
    bio = models.CharField(max_length=255, default='Je suis un artiste passionner par la melodie', blank=True)
    
    aboutMe = models.TextField(null=True, blank=True, max_length=4096, default='Je suis un introverti qui prends de connaitr quelqu\'un avat de commencer le debat')
    
    
    def get_top_songs(self, n):
        # Logique pour récupérer les n meilleures chansons de l'artiste
        pass


    def get_total_views(self):
        return self.totalViews

    def get_popular_videos(self, n):
        # Logique pour récupérer les vidéos les plus populaires de l'artiste
        pass

    def get_total_subscribers(self):
        return self.totalSubscribers

    def get_signed_contracts(self):
        return self.signed_contracts.all()
    
    @classmethod
    def get_most_popular(cls, n):
        # Renvoie les N artistes les plus populaires en fonction du nombre total de vues
        if cls.objects.count() >= n:
            return cls.objects.order_by('-totalViews')[:n]
        else:
            return cls.objects.order_by('-totalViews')
        
    def __str__(self):
        
        return '.'.join(self.alias.split(' '))
    def get_followers_count(self):
        if self.followers.count() > 2:
            return self.followers.count() - 1
        else:
            return self.followers.count()
        
    def get_style(self):
        
        return self.styleMusic.all()
    def get_music(self):
        return self.composers.all()
    
    def count_music(self):
        if self.get_music().count() > 0:
            return self.get_music().count() - 1
        else:
            return self.get_music().count()
        
    def get_last_music_age(self):
        return self.get_music().last().calculate_release_age()
    
    def get_last_music_count_stream(self):
        return self.get_music().last().playCount
    
    @property
    def get_facebook_link(self):
        return self.facebook if self.facebook else ''

    @property
    def get_instagram_link(self):
        return self.instagram if self.instagram else ''

    @property
    def get_tiktok_link(self):
        return self.tiktok if self.tiktok else ''

    @property
    def get_youtube_link(self):
        return self.youtube if self.youtube else ''
    
    # def formatted_phone_number(self):
    #     parsed_number = phonenumbers.parse(self.phoneNumber, "TD")  # "TD" pour le Tchad
    #     country_code = parsed_number.country_code
    #     national_number = str(parsed_number.national_number)
    #     formatted_number = f"+{country_code} {national_number[:2]}{'*' * (len(national_number) - 4)}{national_number[-2:]}"
    #     return formatted_number
    # def phone(self):
    #     parsed_number = phonenumbers.parse(self.phoneNumber, "TD")  # "TD" pour le Tchad
    #     formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    #     return formatted_number

class ProductionHouse(TimeStamps):
    
    reference_id = HashidAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    tiktok = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    
    profileImage = models.ImageField(upload_to='images/artist/cover', blank=True, null=True)
    coverImage = models.ImageField(upload_to='images/artist/profile', blank=True, null=True)
    
    contracts = models.ManyToManyField(Artist, related_name='signed_contracts', blank=True)
    # Nouveaux champs spécifiques
    foundingYear = models.IntegerField(blank=True, null=True)
    founder = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank=True)
 
    def sign_contract(self, artist):
        self.contracts.add(artist)

    def get_signed_artists(self):
        return self.contracts.all()

    def add_copyright(self, holder, registration_number, start_date, end_date):
        copyright = Copyright.objects.create(holder=holder, registration_number=registration_number, start_date=start_date, end_date=end_date, production_house=self)
        copyright.save()
        return copyright
    
    def __str__(self):
        return f"{''.join(self.name.split(' ')).lower()}@{self.reference_id[:4]}"

class Copyright(TimeStamps):
    reference_id = HashidAutoField(primary_key=True, unique=True)
    holder = models.ForeignKey('ProductionHouse', on_delete=models.CASCADE, null=True, blank=True)
    registration_date = models.DateField()
    expiration_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"Copyright for {self.holder}"