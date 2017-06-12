import requests


REGION_CODES = {
    'US': 1,
    'EU': 2,
    'KR': 3,
    'CN': 4,
}


def get_player_id(battletag, region):
    """
    Get the hotslogs unique id assigned to a player.

    :param battletag: the battletag of the player
    :param region: the region of the player ('US', 'EU', 'KR', 'CN')
    """
    battletag = battletag.replace('#', '_').strip()
    region = REGION_CODES[region]

    url = 'https://www.hotslogs.com/API/Players/%s/%s' % (region, battletag)
    data = requests.get(url).json()

    return data['PlayerID']


def get_match_history(player_id):
    """
    Fetch the match history of the provided player id.

    :param player_id: the hotslogs unique id of the player
    """
    _ = 'https://www.hotslogs.com/Player/MatchHistory?PlayerID=%s' % player_id
    return requests.get(_).text
