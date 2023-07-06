from riot import RiotAPI


class SummonerV4(RiotAPI):
    _prefix = "/lol/summoner/v4/summoners/"
    _endpoints = {
        "by_account_id": "by-account/#",
        "by_name": "by-name/#",
        "by_puuid": "by-puuid/#",
        "by_summoner_id": "#", # region ID = summoner ID
    }

    @classmethod
    def by_account_id(cls, platform, account_id):
        return cls._get_data(cls._get_url(platform, "by_account_id", account_id))

    @classmethod
    def by_name(cls, platform, name):
        return cls._get_data(cls._get_url(platform, "by_name", name))
    
    @classmethod
    def by_puuid(cls, platform, puuid):
        return cls._get_data(cls._get_url(platform, "by_puuid", puuid))
    
    @classmethod
    def by_summoner_id(cls, platform, summoner_id):
        return cls._get_data(cls._get_url(platform, "by_summoner_id", summoner_id))
