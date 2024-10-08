from django.db import models
from django.db.models import JSONField


# Create your models here.
class Encounter(models.Model):
    region = models.CharField(max_length=10, db_index=True)
    fight_end = models.IntegerField(db_index=True)
    fight_duration = models.IntegerField(db_index=True)
    boss_name = models.CharField(max_length=64, db_index=True)
    difficulty = models.CharField(max_length=9, db_index=True)
    max_hp = models.BigIntegerField(null=True)
    npc_id = models.IntegerField(null=True)

    def __str__(self):
        return f"Encounter: {self.id} - {self.boss_name}"


class EncounterPlayers(models.Model):
    encounter = models.ForeignKey(
        Encounter, on_delete=models.CASCADE, related_name="players"
    )
    name = models.CharField(max_length=16, db_index=True)
    character_id = models.BigIntegerField(null=True)
    class_id = models.IntegerField(db_index=True)
    subclass = models.CharField(max_length=26, db_index=True, null=True)
    dps = models.IntegerField(db_index=True)
    gear_score = models.FloatField(db_index=True)
    is_dead = models.BooleanField(db_index=True)
    party_num = models.IntegerField()
    display_name = models.BooleanField(db_index=True, default=True)

    def __str__(self):
        return f"Encounter: {self.encounter.id} - Player: {self.name}"


class EncounterPlayerData(models.Model):
    player = models.ForeignKey(
        EncounterPlayers, on_delete=models.CASCADE, related_name="player_data"
    )
    total_damage = models.BigIntegerField()
    casts = models.IntegerField()
    hits = models.IntegerField()
    crits = models.IntegerField()
    back_attacks = models.IntegerField()
    front_attacks = models.IntegerField()
    counters = models.IntegerField()
    buffs = JSONField(default=dict)
    debuffs = JSONField(default=dict)
    skills = JSONField(default=dict)
    shields = JSONField(default=dict)
    absorbs = JSONField(default=dict)

    def __str__(self):
        return f"Encounter: {self.player.encounter.id} - Player: {self.player.name} - Damage: {self.total_damage}"
