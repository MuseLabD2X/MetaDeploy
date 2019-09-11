# Generated by Django 2.2.4 on 2019-08-05 16:09

import django.db.models.deletion
import parler.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("api", "0076_preflight_checks")]

    operations = [
        migrations.AlterField(
            model_name="plantemplatetranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="api.PlanTemplate",
            ),
        ),
        migrations.AlterField(
            model_name="plantranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="api.Plan",
            ),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="api.Product",
            ),
        ),
        migrations.AlterField(
            model_name="siteprofiletranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="api.SiteProfile",
            ),
        ),
        migrations.AlterField(
            model_name="steptranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="api.Step",
            ),
        ),
        migrations.AlterField(
            model_name="versiontranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="api.Version",
            ),
        ),
    ]