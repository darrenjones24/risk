"""
This code defines a number of continents and territories that can be used
in the game of Risk.
"""
import random

north_america = [
    "Alaska",
    "Northwest Territory",
    "Greenland",
    "Alberta",
    "Ontario",
    "Quebec",
    "Western United States",
    "Eastern United States",
    "Central America",
]

south_america = ["Venezuela", "Peru", "Brazil", "Argentina"]

europe = [
    "Iceland",
    "Scandinavia",
    "Ukraine",
    "Great Britian",
    "Northern Europe",
    "Southern Europe",
    "Western Europe",
]

africa = ["North Africa", "Egypt", "East Africa", "Congo", "South Africa", "Madagascar"]

australasia = [
    "Indonesia",
    "New Guinea",
    "Western Australia",
    "Eastern Australia",
]

asia = [
    "Siam",
    "India",
    "China",
    "Mongolia",
    "Japan",
    "Irkutsk",
    "Yakutsk",
    "Kamchatka",
    "Siberia",
    "Afghanistan",
    "Ural",
    "Middle East",
]

continents = africa, asia, north_america, south_america, europe
territories = africa + asia + north_america + south_america + europe + australasia
random.shuffle(territories)


def deal_deck(no_of_humans):
    """
    shuffle deck and deal to the number of humans plus one computer player
    the computer player is the last player so hands[no_of_humans]
    """

    hands = [territories[i :: no_of_humans + 1] for i in range(0, no_of_humans + 1)]
    hands[no_of_humans].sort()
    print(f"Computer has the following {len(hands[no_of_humans])} territories:\n")
    print("\n".join(map(str, hands[no_of_humans])), "\n")
    for player in range(0, no_of_humans):
        hands[player].sort()
        print(f"Player {player} has the following {len(hands[player])} territories:\n")
        print("\n".join(map(str, hands[player])), "\n")
    return hands


def computer_continents(hands, no_of_humans, continents):
    """
    sort the computer player's countries by continent with the continent
    with the most countries first. This is so the continent with the most
    territories gets the most armies.
    """
    comp_cont = []
    for continent_number in range(len(continents)):
        comp_cont.append(
            [x for x in hands[no_of_humans] if x in continents[continent_number]],
        )
    comp_cont = list(filter(None, comp_cont))
    comp_cont.sort(key=len, reverse=True)

    return comp_cont


def start_position(hands, no_of_humans, starting_armies, computer_owns):
    """
    Create a list of armies; one army multiple times
    Distribute that list to the list of countries that the computer owns.
    return a list containing sublists of the country and number of armies.
    If there are more than three players, the computer gets armies in each
    country equal to the number of players.
    """
    if no_of_humans > 3:
        return [[each, no_of_humans] for each in computer_owns]

    n_players = len(hands[no_of_humans])
    armies = [1 for item in range(0, starting_armies)]
    defences = [armies[i::n_players] for i in range(0, n_players)]
    return [list(t) for t in zip(computer_owns, (sum(x) for x in defences))]


def random_continent():
    cont = random.randint(1, 6)
    if cont == 1:
        continent = "North America"
        return continent, north_america
    if cont == 2:
        continent = "South America"
        return continent, south_america
    if cont == 3:
        continent = "Africa"
        return continent, africa
    if cont == 4:
        continent = "Asia"
        return continent, asia
    if cont == 5:
        continent = "Europe"
        return continent, europe
    if cont == 6:
        continent = "Australasia"
        return continent, australasia
