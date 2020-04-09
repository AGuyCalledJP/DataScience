# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Allstarfull(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.CharField(db_column='playerID', max_length=255)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.
    gamenum = models.SmallIntegerField(db_column='gameNum')  # Field name made lowercase.
    gameid = models.CharField(db_column='gameID', blank=True, null=True, max_length=255)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    gp = models.SmallIntegerField(db_column='GP', blank=True, null=True)  # Field name made lowercase.
    startingpos = models.SmallIntegerField(db_column='startingPos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'allstarfull'
        unique_together = (('playerid', 'yearid', 'gamenum', 'gameid', 'lgid'),)


class Appearances(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID')  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    g_all = models.SmallIntegerField(db_column='G_all', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.SmallIntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    g_defense = models.SmallIntegerField(db_column='G_defense', blank=True, null=True)  # Field name made lowercase.
    g_p = models.SmallIntegerField(db_column='G_p', blank=True, null=True)  # Field name made lowercase.
    g_c = models.SmallIntegerField(db_column='G_c', blank=True, null=True)  # Field name made lowercase.
    g_1b = models.SmallIntegerField(db_column='G_1b', blank=True, null=True)  # Field name made lowercase.
    g_2b = models.SmallIntegerField(db_column='G_2b', blank=True, null=True)  # Field name made lowercase.
    g_3b = models.SmallIntegerField(db_column='G_3b', blank=True, null=True)  # Field name made lowercase.
    g_ss = models.SmallIntegerField(db_column='G_ss', blank=True, null=True)  # Field name made lowercase.
    g_lf = models.SmallIntegerField(db_column='G_lf', blank=True, null=True)  # Field name made lowercase.
    g_cf = models.SmallIntegerField(db_column='G_cf', blank=True, null=True)  # Field name made lowercase.
    g_rf = models.SmallIntegerField(db_column='G_rf', blank=True, null=True)  # Field name made lowercase.
    g_of = models.SmallIntegerField(db_column='G_of', blank=True, null=True)  # Field name made lowercase.
    g_dh = models.SmallIntegerField(db_column='G_dh', blank=True, null=True)  # Field name made lowercase.
    g_ph = models.SmallIntegerField(db_column='G_ph', blank=True, null=True)  # Field name made lowercase.
    g_pr = models.SmallIntegerField(db_column='G_pr', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'appearances'
        unique_together = (('yearid', 'teamid', 'playerid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Awardsmanagers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=255)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID')  # Field name made lowercase.
    tie = models.CharField(blank=True, null=True, max_length=255)
    notes = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'awardsmanagers'
        unique_together = (('playerid', 'awardid', 'yearid', 'lgid'),)


class Awardsplayers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=255)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    tie = models.CharField(blank=True, null=True, max_length=255)
    notes = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'awardsplayers'
        unique_together = (('playerid', 'awardid', 'yearid', 'lgid'),)


class Awardssharemanagers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=255)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID')  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    pointswon = models.SmallIntegerField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase.
    pointsmax = models.SmallIntegerField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.SmallIntegerField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'awardssharemanagers'
        unique_together = (('playerid', 'awardid', 'yearid', 'lgid'),)


class Awardsshareplayers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    awardid = models.CharField(db_column='awardID', max_length=255)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID')  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    pointswon = models.TextField(db_column='pointsWon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pointsmax = models.SmallIntegerField(db_column='pointsMax', blank=True, null=True)  # Field name made lowercase.
    votesfirst = models.TextField(db_column='votesFirst', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'awardsshareplayers'
        unique_together = (('playerid', 'awardid', 'yearid', 'lgid'),)


class Batting(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.SmallIntegerField()
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    g_batting = models.SmallIntegerField(db_column='G_batting', blank=True, null=True)  # Field name made lowercase.
    ab = models.SmallIntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.SmallIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.SmallIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.SmallIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.SmallIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.SmallIntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.SmallIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.SmallIntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.SmallIntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.SmallIntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.SmallIntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.SmallIntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'batting'
        unique_together = (('playerid', 'yearid', 'stint'),)


class Battingpost(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=255)
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ab = models.SmallIntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.SmallIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.SmallIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.SmallIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.SmallIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    rbi = models.SmallIntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.SmallIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    ibb = models.SmallIntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.SmallIntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sh = models.SmallIntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.SmallIntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.SmallIntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'battingpost'
        unique_together = (('yearid', 'round', 'playerid'),)


class Collegeplaying(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    schoolid = models.ForeignKey('Schools', models.DO_NOTHING, db_column='schoolID', blank=True, null=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collegeplaying'


class Divisions(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    divid = models.TextField(db_column='divID')  # Field name made lowercase. This field type is a guess.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID')  # Field name made lowercase.
    division = models.CharField(max_length=255)
    active = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'divisions'
        unique_together = (('divid', 'lgid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fielding(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.SmallIntegerField()
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=255)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.SmallIntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.SmallIntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.SmallIntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.SmallIntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.SmallIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.SmallIntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    wp = models.SmallIntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    zr = models.TextField(db_column='ZR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fielding'
        unique_together = (('playerid', 'yearid', 'stint', 'pos'),)


class Fieldingof(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.SmallIntegerField()
    glf = models.SmallIntegerField(db_column='Glf', blank=True, null=True)  # Field name made lowercase.
    gcf = models.SmallIntegerField(db_column='Gcf', blank=True, null=True)  # Field name made lowercase.
    grf = models.SmallIntegerField(db_column='Grf', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldingof'
        unique_together = (('playerid', 'yearid', 'stint'),)


class Fieldingofsplit(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.SmallIntegerField()
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=255)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.SmallIntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.SmallIntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.SmallIntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.SmallIntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.SmallIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.SmallIntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    wp = models.SmallIntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    zr = models.TextField(db_column='ZR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fieldingofsplit'
        unique_together = (('playerid', 'yearid', 'stint', 'pos'),)


class Fieldingpost(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    round = models.CharField(max_length=255)
    pos = models.CharField(db_column='POS', max_length=255)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    innouts = models.SmallIntegerField(db_column='InnOuts', blank=True, null=True)  # Field name made lowercase.
    po = models.SmallIntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    a = models.SmallIntegerField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    e = models.SmallIntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.SmallIntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    tp = models.SmallIntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    pb = models.SmallIntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldingpost'
        unique_together = (('playerid', 'yearid', 'round', 'pos'),)


class Halloffame(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField()
    votedby = models.CharField(db_column='votedBy', max_length=255)  # Field name made lowercase.
    ballots = models.SmallIntegerField(blank=True, null=True)
    needed = models.SmallIntegerField(blank=True, null=True)
    votes = models.SmallIntegerField(blank=True, null=True)
    inducted = models.CharField(blank=True, null=True, max_length=255)
    category = models.CharField(blank=True, null=True, max_length=255)
    needed_note = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'halloffame'
        unique_together = (('playerid', 'yearid', 'votedby'),)


class Homegames(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yearkey = models.IntegerField(blank=True, null=True)
    leaguekey = models.ForeignKey('Leagues', models.DO_NOTHING, db_column='leaguekey', blank=True, null=True)
    teamkey = models.TextField(blank=True, null=True)  # This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    parkkey = models.CharField(blank=True, null=True, max_length=255)
    park = models.ForeignKey('Parks', models.DO_NOTHING, db_column='park_ID', blank=True, null=True)  # Field name made lowercase.
    spanfirst = models.CharField(blank=True, null=True, max_length=255)
    spanlast = models.CharField(blank=True, null=True, max_length=255)
    games = models.IntegerField(blank=True, null=True)
    openings = models.IntegerField(blank=True, null=True)
    attendance = models.IntegerField(blank=True, null=True)
    spanfirst_date = models.DateField(blank=True, null=True)
    spanlast_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'homegames'


class Leagues(models.Model):
    lgid = models.TextField(db_column='lgID')  # Field name made lowercase. This field type is a guess.
    league = models.CharField(max_length=255)
    active = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'leagues'


class Managers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID', blank=True, null=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID')  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    inseason = models.SmallIntegerField()
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    teamrank = models.SmallIntegerField(db_column='teamRank', blank=True, null=True)  # Field name made lowercase.
    plyrmgr = models.CharField(db_column='plyrMgr', blank=True, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'managers'
        unique_together = (('yearid', 'teamid', 'inseason'),)


class Managershalf(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey('People', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID')  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    inseason = models.SmallIntegerField(blank=True, null=True)
    half = models.SmallIntegerField()
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    teamrank = models.SmallIntegerField(db_column='teamRank', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'managershalf'
        unique_together = (('playerid', 'yearid', 'teamid', 'half'),)


class Parks(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parkalias = models.CharField(blank=True, null=True, max_length=255)
    parkkey = models.CharField(blank=True, null=True, max_length=255)
    parkname = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    state = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'parks'


class People(models.Model):
    playerid = models.CharField(db_column='playerID', max_length=255)  # Field name made lowercase.
    birthyear = models.IntegerField(db_column='birthYear', blank=True, null=True)  # Field name made lowercase.
    birthmonth = models.IntegerField(db_column='birthMonth', blank=True, null=True)  # Field name made lowercase.
    birthday = models.IntegerField(db_column='birthDay', blank=True, null=True)  # Field name made lowercase.
    birthcountry = models.CharField(db_column='birthCountry', blank=True, null=True, max_length=255)  # Field name made lowercase.
    birthstate = models.CharField(db_column='birthState', blank=True, null=True, max_length=255)  # Field name made lowercase.
    birthcity = models.CharField(db_column='birthCity', blank=True, null=True, max_length=255)  # Field name made lowercase.
    deathyear = models.IntegerField(db_column='deathYear', blank=True, null=True)  # Field name made lowercase.
    deathmonth = models.IntegerField(db_column='deathMonth', blank=True, null=True)  # Field name made lowercase.
    deathday = models.IntegerField(db_column='deathDay', blank=True, null=True)  # Field name made lowercase.
    deathcountry = models.CharField(db_column='deathCountry', blank=True, null=True, max_length=255)  # Field name made lowercase.
    deathstate = models.CharField(db_column='deathState', blank=True, null=True, max_length=255)  # Field name made lowercase.
    deathcity = models.CharField(db_column='deathCity', blank=True, null=True, max_length=255)  # Field name made lowercase.
    namefirst = models.CharField(db_column='nameFirst', blank=True, null=True, max_length=255)  # Field name made lowercase.
    namelast = models.CharField(db_column='nameLast', blank=True, null=True, max_length=255)  # Field name made lowercase.
    namegiven = models.CharField(db_column='nameGiven', blank=True, null=True, max_length=255)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    bats = models.CharField(blank=True, null=True, max_length=255)
    throws = models.CharField(blank=True, null=True, max_length=255)
    debut = models.CharField(blank=True, null=True, max_length=255)
    finalgame = models.CharField(db_column='finalGame', blank=True, null=True, max_length=255)  # Field name made lowercase.
    retroid = models.CharField(db_column='retroID', blank=True, null=True, max_length=255)  # Field name made lowercase.
    bbrefid = models.CharField(db_column='bbrefID', blank=True, null=True, max_length=255)  # Field name made lowercase.
    birth_date = models.DateField(blank=True, null=True)
    debut_date = models.DateField(blank=True, null=True)
    finalgame_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people'


class Pitching(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey(People, models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    stint = models.SmallIntegerField()
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.SmallIntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.SmallIntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.SmallIntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.SmallIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.SmallIntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.SmallIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.TextField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    era = models.TextField(db_column='ERA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ibb = models.SmallIntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.SmallIntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.SmallIntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.SmallIntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.SmallIntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.SmallIntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.SmallIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.SmallIntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.SmallIntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.SmallIntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pitching'
        unique_together = (('playerid', 'yearid', 'stint'),)


class Pitchingpost(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    playerid = models.ForeignKey(People, models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=255)
    teamid = models.TextField(db_column='teamID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    gs = models.SmallIntegerField(db_column='GS', blank=True, null=True)  # Field name made lowercase.
    cg = models.SmallIntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.SmallIntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.SmallIntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    h = models.SmallIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    er = models.SmallIntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.SmallIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    baopp = models.TextField(db_column='BAOpp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    era = models.TextField(db_column='ERA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ibb = models.SmallIntegerField(db_column='IBB', blank=True, null=True)  # Field name made lowercase.
    wp = models.SmallIntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    hbp = models.SmallIntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    bk = models.SmallIntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    bfp = models.SmallIntegerField(db_column='BFP', blank=True, null=True)  # Field name made lowercase.
    gf = models.SmallIntegerField(db_column='GF', blank=True, null=True)  # Field name made lowercase.
    r = models.SmallIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    sh = models.SmallIntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.SmallIntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    gidp = models.SmallIntegerField(db_column='GIDP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pitchingpost'
        unique_together = (('playerid', 'yearid', 'round'),)


class Salaries(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID')  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    lgid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgID')  # Field name made lowercase.
    playerid = models.ForeignKey(People, models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    salary = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'salaries'
        unique_together = (('yearid', 'teamid', 'lgid', 'playerid'),)


class Schools(models.Model):
    schoolid = models.CharField(db_column='schoolID', max_length=255)  # Field name made lowercase.
    name_full = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    state = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schools'


class Seriespost(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    round = models.CharField(max_length=255)
    teamidwinner = models.CharField(db_column='teamIDwinner', blank=True, null=True, max_length=255)  # Field name made lowercase.
    lgidwinner = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgIDwinner', blank=True, null=True, related_name='lgridwinner')  # Field name made lowercase.
    team_idwinner = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_IDwinner', blank=True, null=True, related_name='team_idwinner')  # Field name made lowercase.
    teamidloser = models.CharField(db_column='teamIDloser', blank=True, null=True, max_length=255)  # Field name made lowercase.
    team_idloser = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team_IDloser', blank=True, null=True, related_name='team_idloser')  # Field name made lowercase.
    lgidloser = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgIDloser', blank=True, null=True, related_name='lgridloser')  # Field name made lowercase.
    wins = models.SmallIntegerField(blank=True, null=True)
    losses = models.SmallIntegerField(blank=True, null=True)
    ties = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seriespost'
        unique_together = (('yearid', 'round'),)


class Teams(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID')  # Field name made lowercase. This field type is a guess.
    franchid = models.ForeignKey('Teamsfranchises', models.DO_NOTHING, db_column='franchID', blank=True, null=True)  # Field name made lowercase.
    divid = models.TextField(db_column='divID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    div = models.ForeignKey(Divisions, models.DO_NOTHING, db_column='div_ID', blank=True, null=True)  # Field name made lowercase.
    teamrank = models.SmallIntegerField(db_column='teamRank', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    ghome = models.SmallIntegerField(db_column='Ghome', blank=True, null=True)  # Field name made lowercase.
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    divwin = models.CharField(db_column='DivWin', blank=True, null=True, max_length=255)  # Field name made lowercase.
    wcwin = models.CharField(db_column='WCWin', blank=True, null=True, max_length=255)  # Field name made lowercase.
    lgwin = models.CharField(db_column='LgWin', blank=True, null=True, max_length=255)  # Field name made lowercase.
    wswin = models.CharField(db_column='WSWin', blank=True, null=True, max_length=255)  # Field name made lowercase.
    r = models.SmallIntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    ab = models.SmallIntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    h = models.SmallIntegerField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.SmallIntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.SmallIntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.SmallIntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.SmallIntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    so = models.SmallIntegerField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    sb = models.SmallIntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.SmallIntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    hbp = models.SmallIntegerField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    sf = models.SmallIntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    ra = models.SmallIntegerField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    er = models.SmallIntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    era = models.TextField(db_column='ERA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cg = models.SmallIntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.SmallIntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    sv = models.SmallIntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    ipouts = models.IntegerField(db_column='IPouts', blank=True, null=True)  # Field name made lowercase.
    ha = models.SmallIntegerField(db_column='HA', blank=True, null=True)  # Field name made lowercase.
    hra = models.SmallIntegerField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    bba = models.SmallIntegerField(db_column='BBA', blank=True, null=True)  # Field name made lowercase.
    soa = models.SmallIntegerField(db_column='SOA', blank=True, null=True)  # Field name made lowercase.
    e = models.IntegerField(db_column='E', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    fp = models.TextField(db_column='FP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(blank=True, null=True, max_length=255)
    park = models.CharField(blank=True, null=True, max_length=255)
    attendance = models.IntegerField(blank=True, null=True)
    bpf = models.IntegerField(db_column='BPF', blank=True, null=True)  # Field name made lowercase.
    ppf = models.IntegerField(db_column='PPF', blank=True, null=True)  # Field name made lowercase.
    teamidbr = models.CharField(db_column='teamIDBR', blank=True, null=True, max_length=255)  # Field name made lowercase.
    teamidlahman45 = models.CharField(db_column='teamIDlahman45', blank=True, null=True, max_length=255)  # Field name made lowercase.
    teamidretro = models.CharField(db_column='teamIDretro', blank=True, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teams'
        unique_together = (('yearid', 'lgid', 'teamid'),)


class Teamsfranchises(models.Model):
    franchid = models.CharField(db_column='franchID', max_length=255)  # Field name made lowercase.
    franchname = models.CharField(db_column='franchName', blank=True, null=True, max_length=255)  # Field name made lowercase.
    active = models.TextField(blank=True, null=True)  # This field type is a guess.
    naassoc = models.CharField(db_column='NAassoc', blank=True, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teamsfranchises'


class Teamshalf(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    yearid = models.SmallIntegerField(db_column='yearID')  # Field name made lowercase.
    lgid = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='lgID')  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID')  # Field name made lowercase. This field type is a guess.
    team = models.ForeignKey(Teams, models.DO_NOTHING, db_column='team_ID', blank=True, null=True)  # Field name made lowercase.
    half = models.CharField(db_column='Half', max_length=255)  # Field name made lowercase.
    divid = models.TextField(db_column='divID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    div = models.ForeignKey(Divisions, models.DO_NOTHING, db_column='div_ID', blank=True, null=True)  # Field name made lowercase.
    divwin = models.CharField(db_column='DivWin', blank=True, null=True, max_length=255)  # Field name made lowercase.
    teamrank = models.SmallIntegerField(db_column='teamRank', blank=True, null=True)  # Field name made lowercase.
    g = models.SmallIntegerField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.SmallIntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.SmallIntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teamshalf'
        unique_together = (('yearid', 'lgid', 'teamid', 'half'),)
