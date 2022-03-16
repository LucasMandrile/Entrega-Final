# Generated by Django 4.0.3 on 2022-03-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_email_alter_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='imagenPost',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes'),
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(to='blog.categoria'),
        ),
    ]