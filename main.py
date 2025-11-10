import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        players = json.load(file)
        for name, player_data in players:
            guild_data = player_data["guild"]
            if guild:
                guild = Guild.objects.get_or_create(name=guild_data["name"], description=guild_data["description"])[0]
            else:
                guild = None
            race_data = player_data["race"]
            race = Race.objects.get_or_create(name=race_data["name"], description=race_data["description"])[0]
            player = Player.objects.create(
                nickname=name,
                email=player_data["email"],
                bio=player_data["bio"],
                race=race,
                guild=guild
            )
            for skill_data in race_data["skills"]:
                skill = Skill.objects.get_or_create(name=skill_data["name"], bonus=skill_data["bonus"])[0]


if __name__ == "__main__":
    main()
