from riot import RiotAPI


class MatchV5(RiotAPI):
    _prefix = "/lol/match/v5/matches/"
    _endpoints = {
        "by_puuid": "by-puuid/#/ids"
    }

    @classmethod
    def by_puuid(cls, region, puuid):
        url = str(cls.region_url(region) + cls._endpoints["by_puuid"]).replace("#", puuid)
        return cls._get_data(url)
