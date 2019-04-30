import constants
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def divide_players(players, teams):
    '''Divides a given iterable of players into equal teams'''
    players_len = len(players)
    num_teams = players_len//len(teams)
    split_team_list = [players[player:player+num_teams] for player in range(0, players_len, num_teams)]
    
    league = dict(zip(constants.TEAMS, split_team_list))

    team_list = constants.TEAMS.copy()
    return league, split_team_list, team_list
    #[l[i:i + n] for i in range(0, len(l), n)]


def welcome():
    app_name = "BASKETBALL TEAM STATS TOOL"
    print("*" * len(app_name))
    print(app_name)
    print("*" * len(app_name), end="\n\n\n")
    print("-" * 10, "MENU", "-" * 10, end="\n\n")


def menu():
    COMMANDS = ["Print Team Stats", "Help", "Quit"]
    for index, item in enumerate(COMMANDS, start = 1):
        print("{}) {}".format(index, item))
    print()


def sub_menu():
    for index, item in enumerate(constants.TEAMS, start=1):
        print("{}) {}".format(index, item))
    print()


def display_team_info(option):
    team = team_list[int(option) - 1]
    players_on_team = list(league[team])
    print("\n\nTEAM: {} Stats".format(team))
    print("_" * 10, "\n\n")
    print("Total Players: {}".format(len(league[team])))
    print()
    print("Player on Team: {}".format(players_on_team))


if __name__ == "__main__":
#Make sure the script doesn't execute when imported; Anything that is a calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file. The main calls to my program should be protected inside dunder main to prevent automatic execution if your script is imported.

# import player data
# clean the data
# balance on total players
# console readability matters
    league, split_team_list, team_list = divide_players(constants.PLAYERS, constants.TEAMS)

    clear_screen()
    welcome()

    while True:
        menu()
        command = input("Please enter the number for the COMMAND that you want >   ")
        print()
        if command == '1':
            sub_menu()
            option = input("Please enter the number for the OPTION that you want >   ")
            display_team_info(option)
            print()
            pass
        elif command == '2':
            continue
        elif command == '3':
            print("Good bye.")
            break
        else:
            print("That is not a valid option. Please try again.")
            continue
