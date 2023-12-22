from django.db import models

class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    AYear = models.IntegerField(null=True, db_column='AYear')
    Semestr = models.IntegerField(null=True, db_column='Semestr')
    DateBeg = models.DateField(null=True, db_column='DateBeg')
    DateEnd = models.DateField(null=True, db_column='DateEnd')
    WeekPeriod = models.TextField(max_length=25, db_column='WeekPeriod')
    TimeBeg = models.TimeField(null=True, db_column='TimeBeg')
    TimeEnd = models.TimeField(null=True, db_column='TimeEnd')
    Teacher = models.TextField(max_length=50, db_column='Teacher')
    ClassRoom = models.TextField(max_length=50, db_column='ClassRoom')
    SGroup = models.TextField(max_length=50, db_column='SGroup')
    SubGroup = models.TextField(max_length=50, null=True, db_column='SubGroup')
    Discipline = models.TextField(max_length=150, db_column='Discipline')
    TypeJob = models.TextField(max_length=50, db_column='TypeJob')
    SubSpecial = models.TextField(max_length=150, null=True, db_column='SubSpecial')
    Kurs = models.IntegerField(null=True, db_column='Kurs')
    DayOfWeek = models.IntegerField(null=True, db_column='DayOfWeek')
    Department = models.TextField(max_length=150, db_column='Department')
    DisciplineShort = models.TextField(max_length=30, null=True, db_column='DisciplineShort')
    TeacherShort = models.CharField(max_length=50, null=True, db_column='TeacherShort')
    OverUnderLine = models.CharField(max_length=10, null=True, db_column='OverUnderLine')
    Faculty = models.TextField(max_length=150, db_column='Faculty')

    class Meta:
        db_table = 'TimeTable'



