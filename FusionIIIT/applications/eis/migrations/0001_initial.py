# Generated by Django 3.1.5 on 2024-07-16 15:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_about',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('about', models.TextField(max_length=1000)),
                ('doj', models.DateField(default=datetime.datetime.now)),
                ('education', models.TextField(max_length=500)),
                ('interest', models.TextField(max_length=500)),
                ('contact', models.CharField(blank=True, max_length=10, null=True)),
                ('github', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='emp_visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('v_type', models.IntegerField(default=1)),
                ('country', models.CharField(default=' ', max_length=500)),
                ('place', models.CharField(default=' ', max_length=500)),
                ('purpose', models.CharField(default=' ', max_length=500)),
                ('v_date', models.DateField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('entry_date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_techtransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('details', models.CharField(default=' ', max_length=500)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_session_chair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('name', models.CharField(default=' ', max_length=500)),
                ('event', models.TextField(default=' ', max_length=2500)),
                ('s_year', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], null=True, verbose_name='year')),
                ('a_month', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, null=True, verbose_name='Month')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('remarks', models.CharField(default=' ', max_length=1000)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_research_projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('ptype', models.CharField(default='Research', max_length=100)),
                ('pi', models.CharField(default=' ', max_length=1000)),
                ('co_pi', models.CharField(default=' ', max_length=1500)),
                ('title', models.TextField(default=' ', max_length=5000)),
                ('funding_agency', models.CharField(default=' ', max_length=250, null=True)),
                ('financial_outlay', models.CharField(default=' ', max_length=150, null=True)),
                ('status', models.CharField(choices=[('Awarded', 'Awarded'), ('Submitted', 'Submitted'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=10)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('date_submission', models.DateField(blank=True, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_research_papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('rtype', models.CharField(choices=[('Journal', 'Journal'), ('Conference', 'Conference')], default='Conference', max_length=500)),
                ('authors', models.CharField(blank=True, max_length=2500, null=True)),
                ('co_authors', models.CharField(blank=True, max_length=2500, null=True)),
                ('title_paper', models.CharField(blank=True, max_length=2500, null=True)),
                ('name', models.CharField(blank=True, max_length=2500, null=True)),
                ('paper', models.CharField(blank=True, max_length=1000, null=True)),
                ('venue', models.CharField(blank=True, max_length=2500, null=True)),
                ('volume_no', models.CharField(blank=True, max_length=500, null=True)),
                ('page_no', models.CharField(blank=True, max_length=500, null=True)),
                ('is_sci', models.CharField(blank=True, choices=[('SCI', 'SCI'), ('SCIE', 'SCIE')], max_length=6, null=True)),
                ('isbn_no', models.CharField(blank=True, max_length=250, null=True)),
                ('doi', models.CharField(blank=True, max_length=1000, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('date_acceptance', models.DateField(blank=True, null=True)),
                ('date_publication', models.DateField(blank=True, null=True)),
                ('year', models.CharField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], max_length=10, null=True)),
                ('a_month', models.CharField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, max_length=500, null=True)),
                ('doc_id', models.CharField(blank=True, max_length=50, null=True)),
                ('doc_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('status', models.CharField(blank=True, choices=[('Published', 'Published'), ('Accepted', 'Accepted'), ('Communicated', 'Communicated')], max_length=15, null=True)),
                ('date_submission', models.DateTimeField(blank=True, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_published_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('p_type', models.CharField(choices=[('Book', 'Book'), ('Monograph', 'Monograph'), ('Book Chapter', 'Book Chapter'), ('Handbook', 'Handbook'), ('Technical Report', 'Technical Report')], max_length=16)),
                ('title', models.CharField(default=' ', max_length=2500)),
                ('publisher', models.CharField(default=' ', max_length=2500)),
                ('pyear', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='year')),
                ('authors', models.CharField(default=' ', max_length=250)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_patents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('p_no', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=1500)),
                ('earnings', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Filed', 'Filed'), ('Granted', 'Granted'), ('Published', 'Published'), ('Owned', 'Owned')], max_length=15)),
                ('p_year', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='year')),
                ('a_month', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, null=True, verbose_name='Month')),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_mtechphd_thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('degree_type', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=250)),
                ('supervisors', models.CharField(max_length=250)),
                ('co_supervisors', models.CharField(blank=True, max_length=250, null=True)),
                ('rollno', models.CharField(max_length=200)),
                ('s_name', models.CharField(max_length=5000)),
                ('s_year', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='year')),
                ('a_month', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, null=True, verbose_name='Month')),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('semester', models.IntegerField(blank=True, default=1, null=True)),
                ('status', models.CharField(blank=True, choices=[('Awarded', 'Awarded'), ('Submitted', 'Submitted'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=10, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_keynote_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Keynote', 'Keynote'), ('Plenary Address', 'Plenary Address')], default='Keynote', max_length=140)),
                ('title', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('venue', models.CharField(max_length=1000)),
                ('page_no', models.CharField(max_length=100)),
                ('isbn_no', models.CharField(max_length=200)),
                ('k_year', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='year')),
                ('a_month', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, null=True, verbose_name='Month')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_expert_lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('l_type', models.CharField(choices=[('Expert Lecture', 'Expert Lecture'), ('Invited Talk', 'Invited Talk')], default='Expert Lecture', max_length=14)),
                ('title', models.CharField(max_length=1000)),
                ('place', models.CharField(max_length=1000)),
                ('l_date', models.DateField(blank=True, null=True)),
                ('l_year', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='year')),
                ('a_month', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, null=True, verbose_name='Month')),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_event_organized',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Training Program', 'Training Program'), ('Seminar', 'Seminar'), ('Short Term Program', 'Short Term Program'), ('Workshop', 'Workshop'), ('Any Other', 'Any Other')], max_length=180)),
                ('name', models.CharField(max_length=1000)),
                ('sponsoring_agency', models.CharField(max_length=150)),
                ('venue', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('Convener', 'Convener'), ('Coordinator', 'Coordinator'), ('Co-Convener', 'Co-Convener')], max_length=11)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_consultancy_projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('consultants', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=1000)),
                ('client', models.CharField(max_length=1000)),
                ('financial_outlay', models.IntegerField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=500, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('status', models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Submitted', 'Submitted'), ('Ongoing', 'Ongoing')], default='Ongoing', max_length=10, null=True)),
                ('remarks', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_confrence_organised',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=500)),
                ('venue', models.CharField(max_length=500)),
                ('k_year', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='year')),
                ('a_month', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, null=True, verbose_name='Month')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('role1', models.CharField(blank=True, choices=[('Advisary Committee', 'Advisary Committee'), ('Program Committee', 'Program Committee'), ('Organised', 'Organised'), ('Conference Chair', 'Conference Chair'), ('Any Other', 'Any Other')], default='Any Other', max_length=200, null=True)),
                ('role2', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=20)),
                ('a_type', models.CharField(choices=[('Award', 'Award'), ('Honour', 'Honour'), ('Prize', 'Prize'), ('Other', 'Other')], default='Other', max_length=180)),
                ('details', models.TextField(default=' ', max_length=1550)),
                ('a_day', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], null=True, verbose_name='Day')),
                ('a_month', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True, verbose_name='Month')),
                ('a_year', models.IntegerField(blank=True, choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='year')),
                ('date_entry', models.DateField(default=datetime.datetime.now)),
                ('achievment_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
