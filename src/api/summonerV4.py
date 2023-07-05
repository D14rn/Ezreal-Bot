from riot import RiotAPI


class SummonerV4(RiotAPI):
    _prefix = "/lol/summoner/v4/summoners/"
    _endpoints = {
        "by_puuid": "by-puuid/#",
        "by_name": "by-name/#",
        "by_region_id": "#", # region ID = summoner ID
        "by_account_id": "by-account/#"
    }

    @classmethod
    def by_name(cls, platform, name):
        return cls._get_data(cls._get_url(platform, "by_name", name))
