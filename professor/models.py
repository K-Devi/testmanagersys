# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Subjects(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subjects'

    def __str__(self):
        return self.name


class Chapters(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    subjectid = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='SubjectId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chapters'

    def __str__(self):
        return self.name


class Questionthemes(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionThemes'

    def __str__(self):
        return self.name


class Chaptertheme(models.Model):
    chaptersid = models.OneToOneField('Chapters', models.DO_NOTHING, db_column='ChaptersId', primary_key=True)  # Field name made lowercase.
    themesid = models.ForeignKey('Questionthemes', models.DO_NOTHING, db_column='ThemesId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChapterTheme'
        unique_together = (('chaptersid', 'themesid'),)

    def __str__(self):
        return self.chaptersid, self.themesid


class Faculties(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Faculties'

    def __str__(self):
        return self.name


class Gradequestion(models.Model):
    gradesid = models.OneToOneField('Grades', models.DO_NOTHING, db_column='GradesId', primary_key=True)  # Field name made lowercase.
    questionsid = models.ForeignKey('Questions', models.DO_NOTHING, db_column='QuestionsId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GradeQuestion'
        unique_together = (('gradesid', 'questionsid'),)




class Grades(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    gradenumber = models.IntegerField(db_column='GradeNumber')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grades'

    def __str__(self):
        return self.gradenumber


class Groupsubject(models.Model):
    groupsid = models.OneToOneField('Groups', models.DO_NOTHING, db_column='GroupsId', primary_key=True)  # Field name made lowercase.
    subjectsid = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='SubjectsId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupSubject'
        unique_together = (('groupsid', 'subjectsid'),)

    def __str__(self):
        return self.groupsid.name, self.subjectsid.name


class Groupuser(models.Model):
    groupsid = models.OneToOneField('Groups', models.DO_NOTHING, db_column='GroupsId', primary_key=True)  # Field name made lowercase.
    usersid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UsersId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroupUser'
        unique_together = (('groupsid', 'usersid'),)



class Groups(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    facultyid = models.ForeignKey(Faculties, models.DO_NOTHING, db_column='FacultyId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groups'

    def __str__(self):
        return self.name


class Images(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)  # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width')  # Field name made lowercase.
    height = models.IntegerField(db_column='Height')  # Field name made lowercase.
    size = models.IntegerField(db_column='Size')  # Field name made lowercase.
    imagebytes = models.BinaryField(db_column='ImageBytes', blank=True, null=True)  # Field name made lowercase.
    uploaddatetime = models.DateTimeField(db_column='UploadDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Images'

    def __str__(self):
        return self.path


class Questiontypes(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuestionTypes'

    def __str__(self):
        return self.name


class Questions(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    topicid = models.ForeignKey('Topics', models.DO_NOTHING, db_column='TopicId')  # Field name made lowercase.
    imageid = models.ForeignKey(Images, models.DO_NOTHING, db_column='ImageId', blank=True, null=True)  # Field name made lowercase.
    questiontypeid = models.ForeignKey(Questiontypes, models.DO_NOTHING, db_column='QuestionTypeId')  # Field name made lowercase.
    questionthemeid = models.ForeignKey(Questionthemes, models.DO_NOTHING, db_column='QuestionThemeId')  # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questions'

    def __str__(self):
        return self.body


class Roleuser(models.Model):
    rolesid = models.OneToOneField('Roles', models.DO_NOTHING, db_column='RolesId', primary_key=True)  # Field name made lowercase.
    usersid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UsersId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoleUser'
        unique_together = (('rolesid', 'usersid'),)




class Roles(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'

    def __str__(self):
        return self.name


class Sessionanswers(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    testsessionid = models.ForeignKey('Testsessions', models.DO_NOTHING, db_column='TestSessionId')  # Field name made lowercase.
    questionid = models.ForeignKey(Questions, models.DO_NOTHING, db_column='QuestionId')  # Field name made lowercase.
    gradeid = models.ForeignKey(Grades, models.DO_NOTHING, db_column='GradeId', blank=True, null=True)  # Field name made lowercase.
    imageid = models.ForeignKey(Images, models.DO_NOTHING, db_column='ImageId', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SessionAnswers'


class Testsessions(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    topicid = models.ForeignKey('Topics', models.DO_NOTHING, db_column='TopicId')  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDatetime')  # Field name made lowercase.
    finishdatetime = models.DateTimeField(db_column='FinishDatetime', blank=True, null=True)  # Field name made lowercase.
    timelimitdatetime = models.DateTimeField(db_column='TimeLimitDatetime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TestSessions'


class Topicrule(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    topicid = models.ForeignKey('Topics', models.DO_NOTHING, db_column='TopicId')  # Field name made lowercase.
    questiontypeid = models.ForeignKey(Questiontypes, models.DO_NOTHING, db_column='QuestionTypeId')  # Field name made lowercase.
    questionthemeid = models.ForeignKey(Questionthemes, models.DO_NOTHING, db_column='QuestionThemeId')  # Field name made lowercase.
    questionscount = models.IntegerField(db_column='QuestionsCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TopicRule'


class Topics(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    chapterid = models.ForeignKey(Chapters, models.DO_NOTHING, db_column='ChapterId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    timelimit = models.DurationField(db_column='TimeLimit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Topics'


class Users(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    middlename = models.TextField(db_column='MiddleName', blank=True, null=True)  # Field name made lowercase.
    ages = models.IntegerField(db_column='Ages')  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate')  # Field name made lowercase.
    imageid = models.ForeignKey(Images, models.DO_NOTHING, db_column='ImageId')  # Field name made lowercase.

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return self.email


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


