from .riot import RiotAPI, RiotRegion


class MatchV5(RiotAPI):
    _prefix = "/lol/match/v5/matches/"
    _endpoints = {
        "by_puuid": "by-puuid/#/ids",
        "by_match_id": "#",
        "by_match_id_timeline": "#/timeline"
    }
    _region_type = RiotRegion

    @classmethod
    def by_puuid(cls, region, puuid):
        return cls._get_data(cls._get_url(region, "by_puuid", puuid))
    
    @classmethod
    def by_match_id(cls, region, match_id):
        return cls._get_data(cls._get_url(region, "by_match_id", match_id))
    
    @classmethod
    def by_match_id_timeline(cls, region, match_id):
        return cls._get_data(cls._get_url(region, "by_match_id_timeline", match_id))
