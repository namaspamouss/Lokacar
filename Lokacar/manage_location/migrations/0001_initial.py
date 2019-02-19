# Generated by Django 2.1.5 on 2019-02-19 15:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_gerant', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=65)),
                ('tresorerie', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date du debut de la location')),
                ('date_fin', models.DateTimeField(verbose_name='date de in de location')),
                ('prix_final', models.DecimalField(decimal_places=2, max_digits=6)),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_location.Agence')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_location.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=20)),
                ('modele', models.CharField(max_length=20)),
                ('prix_loc', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.URLField()),
                ('immatriculation', models.CharField(max_length=8)),
                ('dispo', models.CharField(choices=[('d', 'disponible'), ('l', 'loué'), ('m', 'en maintenance')], max_length=12)),
                ('categorie', models.CharField(choices=[('c', 'citadine'), ('b', 'berline')], max_length=12)),
                ('agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_location.Agence')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='vehicule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_location.Vehicule'),
        ),
    ]
