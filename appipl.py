import requests
import matplotlib.pyplot as plt

COOKIES = {
        "my11c-uid": "d1134d3a-1011-70d4-6a43-7653c9269d9a",
        "my11c-authToken": "eyJhbGciOiJIU.....",  # Truncated for security
        "my11_classic_game": "%7B%0A%20%20%22UserName%22%3A%20%22Anamik..."  # Truncated for security
    }

HEADERS =  {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json;charset=utf-8"
    }

def get_team_names(game_number="4"):
    url = "https://fantasy.iplt20.com/classic/api/user/leagues/2260101/leaderboard"
    params = {
        "optType": "1",
        "gamedayId": game_number,
        "phaseId": "1",
        "pageNo": "1",
        "topNo": "100",
        "pageChunk": "100",
        "pageOneChunk": "100",
        "minCount": "11",
        "leagueId": "2260101"
    }
    
    response = requests.get(url, headers=HEADERS, cookies=COOKIES, params=params)
    players = {}
    for teams in response.json()['Data']['Value']:
        players.update({teams['temid']: teams['temname']+"_"+teams['usrscoid']})
    return players

def get_other_player_stats(game_number="4"):
    players = get_team_names()
    for team_id, player in players.items():
        team_name, social_id = player.split("_")
        url = f"https://fantasy.iplt20.com/classic/api/user/guid/lb-team-get?optType=1&gamedayId={game_number}&tourgamedayId=4&teamId={team_id}&socialId={social_id}"
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        xfer_stats.append({team_name: response.json()['Data']['Value']['subleft']})
    return xfer_stats

def show_data(data):
    
    # Extracting names and values

    # Extracting names and values
    names = [list(d.keys())[0] for d in data]
    values = [list(d.values())[0] for d in data]

    # Sorting data by value in descending order
    sorted_data = sorted(zip(names, values), key=lambda x: x[1], reverse=True)
    sorted_names, sorted_values = zip(*sorted_data)

    # Plot
    plt.figure(figsize=(12, 6))
    bars = plt.bar(sorted_names, sorted_values, color='skyblue')

    # Add numbers on top of bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 2,  # Position slightly inside the bar
                str(bar.get_height()), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

    # Labels and title
    plt.xlabel("Teams", fontsize=12)
    plt.ylabel("Transfers Left", fontsize=12)
    plt.title("Transfers by Team (Descending Order)", fontsize=14)
    plt.xticks(rotation=45, ha="right")

    # Show plot
    plt.show()

xfer_stats = []
players = get_other_player_stats(game_number="4")
show_data(xfer_stats)
