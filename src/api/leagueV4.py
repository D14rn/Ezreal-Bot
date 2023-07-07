from .riot import RiotAPI


class MatchV5(RiotAPI):
    _prefix = "/lol/league/v4/"
    _endpoints = {
        "by_summoner_id": "entries/by-summoner/#",
    }

    @classmethod
    def by_summoner_id(cls, platform, summoner_id):
        return cls._get_data(cls._get_url(platform, "by_summoner_id", summoner_id))
