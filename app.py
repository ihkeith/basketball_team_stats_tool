import constants

def divide_players(constants.PLAYERS, constants.TEAMS):
    '''Divides a given iterable of players into equal teams'''
    #stats_info = [team: player for team in constants.TEAMS for player in constants.PLAYERS]
    league = {}
    [l[i:i + n] for i in range(0, len(l), n)]

if __name__ == "__main__":
#Make sure the script doesn't execute when imported; Anything that is a calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file. The main calls to my program should be protected inside dunder main to prevent automatic execution if your script is imported.

# import player data
# clean the data
# balance on total players
# console readability matters
    #divide_players()

    league = {}

    for player in constants.PLAYERS:
            for team in constants.TEAMS:
                league[team] = constants.PLAYERS
    
    for key, value in league.items():
        print("{}: {}".format(key, value))

    