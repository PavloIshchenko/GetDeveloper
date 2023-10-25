import requests

def read_steam_api_key():
    with open("api_key.txt", "r") as api_key_file:
        steam_api_key = api_key_file.read().strip()
    return steam_api_key

def get_steam_game_developer(game_name, steam_api_key):
    game_name = game_name.lower()
    base_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

    response = requests.get(base_url)
    if response.status_code == 200:
        game_list = response.json().get("applist", {}).get("apps", [])

        for game in game_list:
            if game.get("name").lower() == game_name:
                app_id = game.get("appid")
                game_info_url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
                game_info_response = requests.get(game_info_url)

                if game_info_response.status_code == 200:
                    game_data = game_info_response.json().get(str(app_id), {})
                    if game_data.get("success"):
                        developer = game_data.get("data", {}).get("developers", [])
                        return ", ".join(developer) if developer else "Developer information not found."

    return "Game not found on Steam or developer information is not available."

def main():
    steam_api_key = read_steam_api_key()  # Retrieve the API key
    with open("game_list.txt", "r") as file:
        game_names = [line.strip() for line in file]

    with open("output.txt", "w") as output_file:
        for game_name in game_names:
            print(f"Searching for: {game_name}")  # Print the game name being searched
            developer_info = get_steam_game_developer(game_name, steam_api_key)
            output_line = f"{game_name} = {developer_info}\n"
            output_file.write(output_line)

if __name__ == "__main__":
    main()