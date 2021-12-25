# Version for Data Analysis

import constants
import copy


def team_cleaner():
    clean_list = copy.deepcopy(constants.PLAYERS)
    for count, player in enumerate(clean_list):
        clean_list[count]['height'] = clean_list[count]['height'].removesuffix(" inches")
        clean_list[count]['height'] = int(clean_list[count]['height'])
        if clean_list[count]['experience'] == "YES":
            clean_list[count]['experience'] = True
        else:
            clean_list[count]['experience'] = False
        clean_list[count]['guardians'] = clean_list[count]['guardians'].split(' and ')
    team_maker(clean_list)


def team_maker(clean_list):
    #Create Lists
    team_PANTHERS = []
    team_BANDITS = []
    team_WARRIORS = []
    experienced_players = []
    inexperienced_players = []
    #Split players into experienced and inexperienced
    for player in clean_list:
        if player['experience'] == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    #Divide experienced amongst the teams
    while experienced_players:
        team_PANTHERS.append(experienced_players.pop(0))
        team_BANDITS.append(experienced_players.pop(0))
        team_WARRIORS.append(experienced_players.pop(0))
    #Divide inexperienced amongst the teams
    while inexperienced_players:
        team_PANTHERS.append(inexperienced_players.pop(0))
        team_BANDITS.append(inexperienced_players.pop(0))
        team_WARRIORS.append(inexperienced_players.pop(0))
    
    #Start the menu
    while True:
        selection = input('''\nWelcome To Version 2 of Cody\'s Basketball Tools!
                    \rPlease enter the letter of the action you want to perform.
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
            break
        elif select_team.lower() == 'b':
            name = 'Team Bandits'
            team_players(team_BANDITS, name)
            break
        elif select_team.lower() == 'c':
            name = 'Team Warriors'
            team_players(team_WARRIORS, name)
            break
        elif select_team.lower() == 'd':
            print("Thank you for using this program!")
            exit()
        else:
            print("\n*** Invalid Selection! ***")


def team_players(*team):
    team_name = team[1]
    total_players = len(team[0])
    
    #Experienced and Inexperienced Players Loop
    experienced_players_count = 0
    inexperienced_players_count = 0
    for player in team[0]:
        if player['experience'] == True:
            experienced_players_count += 1
        else:
            inexperienced_players_count += 1
    
    #Begin Average Height
    total_height = 0
    for height in team[0]:
        total_height += height['height']
    average_height = total_height / total_players
    average_height_rounded = round(average_height, 2)
    
    #player names
    player_names = []
    for names in team[0]:
        player_names.append(names['name'])
    
    #guardians
    guardian_names = []
    for names in team[0]:
        guardian_names.append(names['guardians'])
    
    
    
    #Print to Screen
    print(f'''\n=-=-= Team Name: {team_name} =-=-=
       \nTotal Players: {total_players}
       \rTotal Experienced: {experienced_players_count} 
       \rTotal Inexperienced: {inexperienced_players_count}
       \rAverage Height: {average_height_rounded}''')
    print("\nPlayers: " + ', '.join(player_names))
    #print("\nGuardians: " + ', '.join(guardian_names))




if __name__ == '__main__':
    team_cleaner()