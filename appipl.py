import requests

COOKIES = {
        "my11c-uid": "d1134d3a-1011-70d4-6a43-7653c9269d9a",
        "my11c-authToken": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhdXRoIiwiYWNjZXNzVG9rZW4iOiJleUpyYVdRaU9pSkJSRGhEVG5NeFUyNUJjSGdyUW5keU9FUnVTbE5ZUVdnMlFYWkpTRmR5SzI5YWFWTlFRMkZ5U2tkTlBTSXNJbUZzWnlJNklsSlRNalUySW4wLmV5SnpkV0lpT2lKa01URXpOR1F6WVMweE1ERXhMVGN3WkRRdE5tRTBNeTAzTmpVell6a3lOamxrT1dFaUxDSnBjM01pT2lKb2RIUndjenBjTDF3dlkyOW5ibWwwYnkxcFpIQXVZWEF0YzI5MWRHZ3RNUzVoYldGNmIyNWhkM011WTI5dFhDOWhjQzF6YjNWMGFDMHhYM0JwYTFZNWIzUnpaQ0lzSW1Oc2FXVnVkRjlwWkNJNklqY3lhMjgwT1hCak9UVm9jbUZ3TjNCME1HTmxNR2N4ZFhWMklpd2liM0pwWjJsdVgycDBhU0k2SWpCallUa3lZVGRrTFRJek5qQXROR1ZsTmkwNE1XTTBMV0l3WldZNU5qY3dPRFEwTlNJc0ltVjJaVzUwWDJsa0lqb2lZVGxtTURGaVpqQXROemcxTnkwME1EQmtMV0ZoTUdFdE5ESmpOVFkxTUdNeU4yWTBJaXdpZEc5clpXNWZkWE5sSWpvaVlXTmpaWE56SWl3aWMyTnZjR1VpT2lKaGQzTXVZMjluYm1sMGJ5NXphV2R1YVc0dWRYTmxjaTVoWkcxcGJpSXNJbUYxZEdoZmRHbHRaU0k2TVRjME1qZzJNVEkxT1N3aVpYaHdJam94TnpReU9UUTNOalU1TENKcFlYUWlPakUzTkRJNE5qRXlOVGtzSW1wMGFTSTZJbVEzTWpkaFlXWmpMVGN6T0RBdE5HUTVNaTFoWmpnd0xUUmlZV0psTkRKbVpURmpNQ0lzSW5WelpYSnVZVzFsSWpvaVpERXhNelJrTTJFdE1UQXhNUzAzTUdRMExUWmhORE10TnpZMU0yTTVNalk1WkRsaEluMC5rQlFqVFBqYTJ2Nlc2elJ4bjJMb2FxZ2tCdkx3V2NnOXV3VmpVQmRvXzMxNzZaLWRDV3MtZENpSEtTZ2kzNi1BRHdROEl5UzZVa2pWdjZYZmpLc2oxdkVxOVhoQURtRXY4Vmo2TS1IRG9EUF84UjAzSzJoSjBNS2FrOHdNNDY2LVdrVGMxMVFIekN4V1JUUTNmNTJ0NFJqb0hOcERWT2tXclh1dkpiSmNINnBjU05qSzFNbUg2RUE3Nzg0cGZWdW94eXk1ekxyckNZc1lUX2NVenlPb3NRalptOTMwX1NieldaUtaQ3dGNnM2V2lILWtkQXhqOXVmN1p2bmlESjRRN1JmY3JmY2NsVVR3M0NBTVZKanJwSld6aFFpZG5oWjQyQ0pRS0dWV09ZYndBN2hjUkdXdkFCV1VSV0VVN0ZqQlFuVWxoRzFWbTNPYzZQaXFUQy16TkEiLCJ1c2VySWQiOiJkMTEzNGQzYS0xMDExLTcwZDQtNmE0My03NjUzYzkyNjlkOWEiLCJpc0ludGxVc2VyIjp0cnVlLCJyZWZyZXNoVG9rZW4iOiJleUpqZEhraU9pSktWMVFpTENKbGJtTWlPaUpCTWpVMlIwTk5JaXdpWVd4bklqb2lVbE5CTFU5QlJWQWlmUS5PYUFmOHRQSUVfeUJGRXFDSy1BX29pVjhNbUpkQXA1c0NQT2szbnU1LTN1SThDQWVWc3AzclF6NmdScmNRYTBmbU5LZXcxT21hVzlOOGc1VWxqWERtNzcwVzNxNldnTDBPVTkxeEpMd1l2WE8wajJDSUo0R2d5LVkyd05iWTBJVjUtYUh3b1hHUk8wV2VPdWdKNld5dGh0TkQ4akd6RFQza1pISGI0eWJGUE9KQ194TWJQZUJSMFFTWkM2Nmc2dFJPU1pmQlhYNzFYNVVqcTVTTEM1SGE1a2hhaFhYekxxaEttcXZmazdWRWd6MU96Ti1SRndXaTdIbXNUd1l4a2dXaU5oaGVSc1lLeWVnampKRGpyanV0ZzRqdVBSR3ZSMFI0MEZhcGdUVm5PTEZmOWFURkdLWVg1bTNoaHFlVm1sRXloZzVRbmxLUkxSbmx4TjUxWmF5TWcuRldpS0VHTXd3YU1DSWlxSC5iNTdmdmFwVHNqVUt5aFFBVXFueW02V2FBZk1TNmo4UG1zTU5ibDBoWWU1TFdGdTBlN0x1clFJNWR0UVBxTFVjajB1MFk1RHVNY0FRMFdFTkR6Zjl6X011NFhzaWFNeHpONDcwUmxpVnpLc040dThlMVdnT0hpcmljTXFMbnRLN2JLeDNHWHlPNXhJZHBGdDFtbk51Y2JZdjZiSWxsTFl3a2NoaVgydzkxU1hsbXRhTzBRcXBMWjZNRHZUZXB1YTlWeTR6QS1jSWd2Q1c3aHRHbU40dGs3Y01VTmZiOXNSbC1DcnNzYlE3Xzh0RFN0MEJoanc2b2d4V3Y0VThKSzJsbWNLVkVMaXdqeV84bEN6SnB1WXFlTHJDZFItak9DSE5IV3lrbTE3Vkk5QWdBVmFZVDRIeEEzVVZiRUxlWW53OG5KQVFNb0ZoLThaS3RSQzhtQjdybWZBQTRoZko4R3F5SGNtemcyLW5vT0ZJeXVHbVo1Ym5yeVJPQXV0ODBfQVM2MTZSc2QyaHotSnhmODI4bTVzZXlwZjhrUVJQY29Bc1pJZ25aSnlETnBDMm96ZzZwRUxvejVjTXUtVFJmN2tMN19fV3NFeDB4eUpiaWhwcGxGYzdCc0k3OUQ5ZFF4dXlXSHBZOFhfakxxRmdvTkJUZlBYcnpsNl85Z0hDNTA0Ty16cjdzaE43VGM1YThjcFBNLUU4LWNVZnBIWGUyODhjTi1WRVRLc0bicXYwSmdrUC1jWUg3QnFQREdPZjlIMjBhRTZrOUU5MFM2cU9BaE5ydG02RjRMODAxZG9xemFHTi1TQlpKTWpScHd5LVc3WTlfcFF1dzZJSnMwVG5HWDQxQjZRcjZMR3RfVGRKOXRHejF5SExrQ3JWQU9BNUlPMmlGYm4yLXpQU2tKTjFBNVdNYWFRcUJRN0hzNlpwdlZhRUxfZkktSGZyVjlxVHlHVHVnQ08xclVac0JfT0pnWGU0d1FvQXZ5aVd3S2l4RFlZM2dLY3J3VERNVW1wcmJZdmpjendUOFRmS2d6STRIUnFTdEM3MEZiRm91d1ZqZjgwbU4xLWZCV1pEN2tGenU1NkdzN2IxQzV3Nm0zNmhsSDlwZVBsU2YzTE0tclcxaldxUDk3X0NZVzdVVG54QzlwME4wLTNLYWxIdTRJNXBOMzlTTms0azB6bW5JT0F6Q1pEdHhRUG9PaVcxT3U5UWFFZjVGbXZfMGVVSkxYT2hnNTB0V25wWW40a0NYS2lBVHpoaHpjNkp3cEdNclRrSUpHM0xTbXBXVnFKWHpwWEEyaC04Q2tuejVVRERqUVk1OFV4TzJWNzdnTVZCNFJXbnJTVElkYWN4dWdyNGFFLVUyX2k0bE5aLU0wN3RxSUwxWkxRczNONDkxcS1qOTU2V25ybFlmN2EtTk1jdU05ZkhNSGVKM0FDLTdwSW13Y0ttMmNRUERiT091WnZGb2EwWVRNSzJnRHR3N1ZBbmJUR09mdHdDM1VvUnluZ3FMY0VGZS1wMzRFel8zSm5YSGwtRVhVVWxtZjAza1o2UFE5SzNja21MRVFjNl85VGNZbC1yN21sd3pHX2JUeWdkZGdLWGlMeDVyajRwaW01RWt2OExfM21QMDhRQTNId1JSRUFVTzZmbkJmc0k5aE1FLVRwTWs0UTNSZkhVa2g1dnJZQnVXaTZIM0Y3OWwzNXJhYXFoQjY3V082dVQxWklvR01EeDVKcnZDdmw5R3JJalZ2X2F5WDUxdFpicFJKNUw0dVNOazhYd1pFNmEzaGhoU3FzLXhlWS51UUVfWkdOTnhPTjVNMFByWm9YSGF3IiwiaWF0IjoxNzQyODYxMjU5LCJleHAiOjE3NDI5NDc2NTl9.2g-qAIH1MRBssBiZeVoJAPxqIdIyjxInxc7PTNhnoqQ",  # Truncated for security
        "my11_classic_game": "%7B%0A%20%20%22UserName%22%3A%20%22Anamik%22%2C%0A%20%20%22HasTeam%22%3A%201%2C%0A%20%20%22TeamName%22%3A%20%22Anamik%22%2C%0A%20%20%22FavTeamId%22%3A%20%221110%22%2C%0A%20%20%22SocialId%22%3A%20%22d1134d3a-1011-70d4-6a43-7653c9269d9a%22%2C%0A%20%20%22GUID%22%3A%20%22771cfa22-fde7-11ef-836c-020d19adcd31%22%2C%0A%20%20%22ActiveTour%22%3A%20null%2C%0A%20%20%22IsTourActive%22%3A%200%2C%0A%20%20%22UserId%22%3A%20%22EF22A67819675C%22%2C%0A%20%20%22TeamId%22%3A%20%22EF22A67819675C%22%2C%0A%20%20%22ProfileURL%22%3A%20%22%22%2C%0A%20%20%22TeamName_Allow%22%3A%20%220%22%2C%0A%20%20%22Version%22%3A%20%224%22%2C%0A%20%20%22IsIndian%22%3A%20%220%22%0A%7D"  # Truncated for security
    }

HEADERS =  {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json;charset=utf-8"
    }

def get_team_names(game_number="4", leaguid="2260101"):
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
        "leagueId": leaguid
    }
    
    response = requests.get(url, headers=HEADERS, cookies=COOKIES, params=params)
    players = {}
    for teams in response.json()['Data']['Value']:
        players.update({teams['temid']: teams['temname']+"_"+teams['usrscoid']})
    return players

def get_other_player_stats(game_number="4"):
    import requests

    players = get_team_names(game_number=game_number, leaguid="54390105")
    for team_id, player in players.items():
        team_name, social_id = player.split("_")
        url = f"https://fantasy.iplt20.com/classic/api/user/guid/lb-team-get?optType=1&gamedayId={game_number}&tourgamedayId=4&teamId={team_id}&socialId={social_id}"
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        xfer_stats.append({team_name: response.json()['Data']['Value']['subleft']})
    return xfer_stats

def show_data(data):
    import matplotlib.pyplot as plt
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
    plt.title("Scores by Team (Descending Order)", fontsize=14)
    plt.xticks(rotation=45, ha="right")

    # Show plot
    plt.show()

def find_game_number():
    url = 'https://fantasy.iplt20.com/classic/api/feed/tour-fixtures?lang=en&liveVersion=03242025191835'
    response = requests.get(url, headers=HEADERS, cookies=COOKIES)
    for games in response.json()['Data']['Value']:
        if not games['IsLive']:
           return games['Matchday']

xfer_stats = []
game_number = str(find_game_number() - 1) # Last game marked as Completed
players = get_other_player_stats(game_number)
show_data(xfer_stats)
