import constants
import os

# http://wordaligned.org/articles/slicing-a-list-evenly-with-python
#### great resource: I tried figuring out how to divide the list and thought about slices, but didn't think of using steps
# https://stackoverflow.com/questions/7271385/how-do-i-combine-two-lists-into-a-dictionary-in-python
#### I used this one for making my league dictionary
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def divide_players(players, teams):
    '''Divides a given iterable of players into equal teams'''
    team_list = constants.TEAMS.copy()
    players_len = len(players)
    num_teams = players_len//len(teams)
    split_team_list = [players[player:player+num_teams] for player in range(0, players_len, num_teams)]
    
    league = dict(zip(team_list, split_team_list))

    
    return league, split_team_list, team_list
    #[l[i:i + n] for i in range(0, len(l), n)]


def welcome():
    app_name = "BASKETBALL TEAM STATS TOOL"
    print("*" * len(app_name))
    print(app_name)
    print("*" * len(app_name), end="\n\n\n")
    print("-" * 10, "MENU", "-" * 10, end="\n\n")


def menu():
    COMMANDS = ["Display Team Stats", "Help", "Quit"]
    for index, item in enumerate(COMMANDS, start = 1):
        print("{}) {}".format(index, item))
    print()


def sub_menu():
    for index, item in enumerate(team_list, start=1):
        print("{}) {}".format(index, item))
    print()


def display_team_info(option):
    try:
        team = team_list[int(option) - 1]
        players_on_team = [dic["name"] for dic in league[team]]
        print("\n\nTEAM: {} Stats".format(team))
        print("-" * 26, "\n")
        print("Total Players: {}".format(len(league[team])))
        print()
        print("Player on Team: ", end="")
        for player in players_on_team:
            if player == players_on_team[-1]:
                print(player, end="\n\n")
            else:
                print(player, end=", ")
        input("Press Enter to continue.")
        clear_screen()
        welcome()
    except IndexError:
        print("\nThat is not a valid option. Please try again. \n")
    except ValueError:
        print("\nThat is not a valid option. Please try again. \n")


if __name__ == "__main__":
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
            clear_screen()
            welcome()
            continue
        elif command == '3':
            print("Good bye.\n\n")
            break
        else:
            print("\nThat is not a valid option. Please try again. \n")
            continue
