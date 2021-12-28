# Version for Data Analysis, PEP 8 Verified

import constants
import copy


def team_cleaner():
    clean_list = copy.deepcopy(constants.PLAYERS)
    for count, player in enumerate(clean_list):
        clean_list[count]['height'] = clean_list[count]['height']\
            .removesuffix(" inches")
        clean_list[count]['height'] = int(clean_list[count]['height'])
        if clean_list[count]['experience'] == "YES":
            clean_list[count]['experience'] = True
        else:
            clean_list[count]['experience'] = False
        clean_list[count]['guardians'] = clean_list[count]['guardians'] \
            .split(' and ')

    team_maker(clean_list)


def team_maker(clean_list):
    # Create Lists
    team_PANTHERS = []
    team_BANDITS = []
    team_WARRIORS = []
    experienced_players = []
    inexperienced_players = []
    # Split players into experienced and inexperienced
    for player in clean_list:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    # Divide experienced among the teams
    while experienced_players:
        team_PANTHERS.append(experienced_players.pop(0))
        team_BANDITS.append(experienced_players.pop(0))
        team_WARRIORS.append(experienced_players.pop(0))
    # Divide inexperienced amongst the teams
    while inexperienced_players:
        team_PANTHERS.append(inexperienced_players.pop(0))
        team_BANDITS.append(inexperienced_players.pop(0))
        team_WARRIORS.append(inexperienced_players.pop(0))

    # Start the menu
    while True:
        selection = input('''\nWelcome To Cody\'s Basketball Tools!
                    \nPlease enter the letter of the action
                    \ryou want to perform.
                    \rEnter A for Team Stats
                    \rEnter B to exit the program
                    \rEnter Command: ''')
        if selection.lower() == 'a':
            team_select(team_PANTHERS, team_BANDITS, team_WARRIORS)
            break
        elif selection.lower() == 'b':
            print("Thank you for using the program!")
            exit()
        else:
            print("\n*** Invalid Selection ***")


def team_select(team_PANTHERS, team_BANDITS, team_WARRIORS):
    while True:
        select_team = input('''\nPlease Enter the Letter of the Team you want to view.
        \rA) Panthers
        \rB) Bandits
        \rC) Warriors
        \rD) Quit
        \nEnter: ''')
        if select_team.lower() == 'a':
            name = 'Team Panthers'
            team_players(team_PANTHERS, name)
            input("Press Enter to Return to Menu... ")
        elif select_team.lower() == 'b':
            name = 'Team Bandits'
            team_players(team_BANDITS, name)
            input("Press Enter to Return to Menu... ")
        elif select_team.lower() == 'c':
            name = 'Team Warriors'
            team_players(team_WARRIORS, name)
            input("Press Enter to Return to Menu... ")
        elif select_team.lower() == 'd':
            print("Thank you for using this program! \n")
            exit()
        else:
            print("\n*** Invalid Selection! ***")


def short_to_tall(h):
    return h['height']


def team_players(*team):
    team_name = team[1]
    total_players = len(team[0])

    # sort by height
    sort_height = team[0].sort(key=short_to_tall)

    # Experienced and Inexperienced Players Loop
    experienced_players_count = 0
    inexperienced_players_count = 0
    for player in team[0]:
        if player['experience']:
            experienced_players_count += 1
        else:
            inexperienced_players_count += 1

    # Begin Average Height
    total_height = 0
    for height in team[0]:
        total_height += height['height']
    average_height = total_height / total_players
    average_height_rounded = round(average_height, 2)

    # Player names
    player_names = []
    for names in team[0]:
        player_names.append(names['name'])

    # Guardians
    guardian_names = []
    for names in team[0]:
        guardian_names.extend(names['guardians'])

    # Print to Screen
    print(f'''\n=-=-= Team Name: {team_name} =-=-=
       \nTotal Players: {total_players}
       \rTotal Experienced: {experienced_players_count}
       \rTotal Inexperienced: {inexperienced_players_count}
       \rAverage Height: {average_height_rounded}''')
    print('''\n* Arranged Shortest to Tallest: *
            \rPlayers: ''' + ', '.join(player_names))
    print("\rGuardians: " + ', '.join(guardian_names) + '\n')

if __name__ == '__main__':
    team_cleaner()
