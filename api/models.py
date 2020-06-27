from django.db import models

class License(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.TextField(db_column='NAME',max_length=50,null=False)
    price = models.FloatField(db_column='PRICE',null=False)

    class Meta:
        managed=True
        db_table="LICENSE"

class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nick = models.TextField(db_column='NICKNAME',max_length=35,null=False)
    email = models.TextField(db_column='EMAIL',max_length=100,null=False)
    firebase_uid = models.TextField(db_column='FIREBASE_UID',max_length=200,null=False)
    created_at = models.DateTimeField(db_column='CREATED_AT',blank=True,null=True,)
    license = models.ForeignKey(License,db_column='LICENSE',null=False,on_delete=models.PROTECT)

    class Meta:
        managed=True
        db_table="USERS"

class Instrument(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.TextField(db_column='NAME', max_length=25, null=False)

    class Meta:
        managed=True
        db_table="INSTRUMENTS"

class Genre(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.TextField(db_column='NAME', max_length=35, null=False)

    class Meta:
        managed=True
        db_table="GENRE"

class Status(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.TextField(db_column='NAME', max_length=35, null=False)

    class Meta:
        managed=True
        db_table="STATUS"

class Music(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.TextField(db_column='NAME', max_length=50, null=False)
    duration = models.IntegerField(db_column='DURATION',null=True)
    created_at = models.DateTimeField(db_column='CREATED_AT',blank=True,null=True,)
    deleted = models.BooleanField(db_column='DELETED',default=False,null=False)
    image = models.CharField(db_column='IMG_URL',max_length=100, null=False)
    music_url = models.CharField(db_column='MUSIC_URL', max_length=100, null=False)

    class Meta:
        managed=True
        db_table="MUSIC"

class MusicInstrument(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    music = models.ForeignKey(Music,db_column='ID_MUSIC',null=False,on_delete=models.PROTECT)
    instrument = models.ForeignKey(Instrument,db_column='ID_INSTRUMENT',null=False,on_delete=models.PROTECT)

    class Meta:
        managed=True
        db_table="MUSIC_INSTRUMENT"

class MusicGenre(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    music = models.ForeignKey(Music,db_column='ID_MUSIC',null=False,on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre,db_column='ID_GENRE',null=False,on_delete=models.PROTECT)

    class Meta:
        managed=True
        db_table="MUSIC_GENRE"

class MusicUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    music = models.ForeignKey(Music,db_column='ID_MUSIC',null=False,on_delete=models.PROTECT)
    user = models.ForeignKey(User,db_column='ID_USER',null=False,on_delete=models.PROTECT)
    status = models.ForeignKey(Status,db_column='ID_STATUS',null=False,on_delete=models.PROTECT)

    class Meta:
        managed=True
        db_table="MUSIC_USER"

