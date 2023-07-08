from .riot import RiotAPI


class MatchV5(RiotAPI):
    _prefix = "/lol/spectator/v4/"
    _endpoints = {
        "by_summoner_id": "active-games/by-summoner/#",
    }

    @classmethod
    def by_summoner_id(cls, region, summoner_id):
        return cls._get_data(cls._get_url(region, "by_summoner_id", summoner_id))
