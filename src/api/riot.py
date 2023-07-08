from abc import ABC
from enum import Enum

import requests


class APIKeyNotSetError(Exception):
    pass

class SummonerNotFoundError(Exception):
    pass

#class Rank

class RankedQueue(Enum):
    RANKED_SOLO_5x5 = "Ranked Solo/Duo"
    RANKED_FLEX_SR = "Ranked Flex"

class RiotPlatform(Enum):
    EUW = "euw1"; EUNE = "eun1"; TR = "tr1"; RU = "ru"
    KR = "kr"; JP = "jp1"
    NA = "na1"; BR = "br1"; LAN = "la1"; LAS = "la2"
    OCE = "oc1"; PH = "ph2"; SG = "sg2"; TH = "th2"; VN = "vn2"

class RiotRegion(Enum):
    EUW = EUNE = TR = RU = "europe"
    KR = JP = "asia"
    NA = BR = LAN = LAS = "americas"
    OCE = PH = SG = TH = VN = "sea"

class RiotAPI(ABC):
    # todo add requests Session (for rate limiting)
    _base_url = "https://#.api.riotgames.com"
    _prefix = ""
    __api_key = ""
    _endpoints = {}
    _region_type = RiotPlatform # override this with RiotRegion if the API endpoint requires a region

    @classmethod 
    def initialize_key(cls, api_key: str):
        cls.__api_key = api_key
 
    @staticmethod
    def _replace_url(url: str, new: str):
        return url.replace("#", new, 1)
    
    @classmethod
    def _get_data(cls, url: str):
        response = requests.get(url, headers=cls._get_headers())
        if response.ok:
            return response.json()
    
    @classmethod
    def _get_headers(cls):
        return {"X-Riot-Token": cls.__api_key}
    
    @classmethod
    def _get_url(cls, region, endpoint, replace_by):
        return cls._replace_url(cls._base_url, region.value) + cls._prefix + cls._replace_url(cls._endpoints[endpoint], replace_by)

class LeagueAssets:
    @staticmethod
    def icon_url(icon_id):
        return f"http://ddragon.leagueoflegends.com/cdn/13.1.1/img/profileicon/{icon_id}.png"
