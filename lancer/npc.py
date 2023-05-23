import random
import argparse


def parse_arguments():

    p = argparse.ArgumentParser()

    p.add_argument('-n', '--name', action='store_true', help='Generate first and last name')
    p.add_argument('-m', '--mech', action='store_true', help='Generate mech with callsign and npc class')
    p.add_argument('-t', '--team', action='store_true', help='Generate a team name')
    p.add_argument('-g', '--team_generate', action='store_true', help='Generate a mech team of 5')
    p = p.parse_args()
    return p


def generate_name():
    """
    Generate an name from firstname.txt/lastname.txt
    """
    f_names = []
    l_names = []

    with open('firstnames.txt') as fh:
        for n in fh.readlines():
            f_names.append(n.strip())
    with open('lastnames.txt') as fh:
        for n in fh.readlines():
            l_names.append(n.strip())

    first_name = f_names[random.randint(0,len(f_names)-1)]
    last_name = l_names[random.randint(0,len(l_names)-1)]

    return [first_name, last_name]

def generate_mech():
    """
    Generate NPC mech including callsign and NPC base class
    """

    m_names = []
    m_types = []
    m_callsigns = []

    with open('mechnames.txt') as fh:
        for n in fh.readlines():
            m_names.append(n.strip())
    with open('mechtypes.txt') as fh:
        for n in fh.readlines():
            m_types.append(n.strip())
    with open('callsigns.txt') as fh:
        for n in fh.readlines():
            m_callsigns.append(n.strip())

    mech_name = m_names[random.randint(0,len(m_names)-1)]
    mech_type = m_types[random.randint(0,len(m_types)-1)]
    mech_callsign = m_callsigns[random.randint(0,len(m_callsigns)-1)]

    return [mech_name,mech_type, mech_callsign]

def generate_team():
    """
    Generate NPC team name
    """

    team_names = []

    with open('teamnames.txt') as fh:
        for n in fh.readlines():
            team_names.append(n.strip())

    team_name = team_names[random.randint(0,len(team_names)-1)]

    return [team_name]

def main(args):
    """
    npc runner. accepts args and generates content based on that input
    """
    if args.team_generate:
        team = generate_team()
        print(f"TEAM: {team[0]}")
        for i in range(5):
            print(f"## MEMBER {i} ##")
            name = generate_name()
            print(f"FIRST: {name[0]} | LAST: {name[1]}")
            mech = generate_mech()
            print(f"MECH NAME: {mech[0]} | CLASS: {mech[1]} | CALLSIGN: {mech[2]}")
            
    else:
        if args.name:
            name = generate_name()
            print(f"FIRST: {name[0]} | LAST: {name[1]}")
        if args.mech:
            mech = generate_mech()
            print(f"MECH NAME: {mech[0]} | CLASS: {mech[1]} | CALLSIGN: {mech[2]}")
        if args.team:
            team = generate_team()
            print(f"TEAM: {team[0]}")


if __name__ == '__main__':
    args = parse_arguments()
    random.seed()

    main(args)

