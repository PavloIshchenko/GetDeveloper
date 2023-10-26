# Game Developer Finder

Game Developer Finder is a Python script that retrieves the developer information for a list of games from the Steam platform using the Steam Web API.

## Prerequisites

Before using this script, you'll need the following:

- Python 3.x
- A Steam Web API key, which you can obtain by [registering for a Steam Web API account](https://steamcommunity.com/dev/apikey).

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git

2. Install the required Python libraries:

   ```bash
   pip3 install requests

3. Plcae your actual Steam Web API key in api_key.txt.

4. Run the script:
   ```bash
   python3 developers.py

5. The script will retrieve the developer information for each game listed in game_list.txt and save the results in the "output.txt" file.

## Sample game_list.txt

   ```makefile
   Dota 2
   Counter-Strike: Global Offensive
   Half-Life

