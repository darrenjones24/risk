from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PlayerForm, LoseCountryForm, GainCountryForm
from .neutral_player import *

def players(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            number_of_humans = int(request.POST["number_of_players"])
            request.session["number_of_humans"] = number_of_humans
            starting_armies = -5 * (number_of_humans + 1) + 50
            request.session["starting_armies"] = starting_armies
            hands = deal_deck(number_of_humans)
            comp_cont = computer_continents(hands, number_of_humans, continents)
            request.session["comp_cont"] = comp_cont
            computer_owns = (item for sublist in comp_cont for item in sublist)
            computer_start_position = start_position(
                hands,
                number_of_humans,
                starting_armies,
                computer_owns,
            )
            request.session["computer_start_position"] = computer_start_position
            for player in range(0, number_of_humans):
                hands[player].sort()
            request.session["hands"] = hands

            return HttpResponseRedirect("/show_positions")

    else:
        form = PlayerForm()
        return render(request, "website/players.html", {"form": form})


def comp_gain_country(request):
    if not request.session or not request.session.session_key:
        return HttpResponseRedirect("/players")

    hands = request.session.get("hands")
    number_of_humans = request.session.get("number_of_humans")

    form = GainCountryForm(request.POST, countries=hands)

    if request.method == "POST":
        comphand = hands[number_of_humans]
        comphand.append(request.POST["gain"])
        request.session["hands"][number_of_humans] = comphand
        request.session.modified = True
        return HttpResponseRedirect("/current_positions")

    else:
        return render(request, "website/comp_gain.html", {"form": form})


def comp_lose_country(request):
    if not request.session or not request.session.session_key:
        return HttpResponseRedirect("/players")
    hands = request.session.get("hands")
    number_of_humans = request.session.get("number_of_humans")
    form = LoseCountryForm(request.POST, countries=hands[number_of_humans])

    if request.method == "POST":
        comphand = [
            country
            for country in hands[number_of_humans]
            if country != request.POST["loss"]
        ]
        request.session["hands"][number_of_humans] = comphand
        # hack add the country to player one
        request.session["hands"][0].append(request.POST["loss"])
        request.session.modified = True

        return HttpResponseRedirect("/current_positions")
    else:
        return render(request, "website/comp_lose.html", {"form": form})


def reinforce(request):
    if not request.session or not request.session.session_key:
        return HttpResponseRedirect("/players")
    hands = request.session.get("hands")
    new_armies = random.randint(1, 6)
    cont = random_continent()
    hands = request.session.get("hands")
    number_of_humans = request.session.get("number_of_humans")
    reinforced = [country for country in cont[1] if country in hands[number_of_humans]]
    if not reinforced:
        return render(
            request,
            "website/attack.html",
            {
                "hands": hands,
                "cont": cont[0],
                "new_armies": new_armies,
            },
        )

    else:
        return render(
            request,
            "website/reinforce.html",
            {
                "hands": hands,
                "cont": cont[0],
                "new_armies": new_armies,
            },
        )


def show_positions(request):
    if not request.session or not request.session.session_key:
        return HttpResponseRedirect("/players")
    if request.method == "POST":
        return HttpResponseRedirect("/reinforce")

    number_of_humans = request.session.get("number_of_humans")
    starting_armies = request.session.get("starting_armies")
    computer_start_position = request.session.get("computer_start_position")
    hands = request.session.get("hands")
    return render(
        request,
        "website/show_positions.html",
        {
            "number_of_players": number_of_humans,
            "starting_armies": starting_armies,
            "computer_start_position": computer_start_position,
            "range": range(0, number_of_humans),
            "hands": hands,
        },
    )


def current_positions(request):
    if not request.session or not request.session.session_key:
        return HttpResponseRedirect("/players")

    number_of_humans = request.session.get("number_of_humans")
    hands = request.session.get("hands")
    return render(
        request,
        "website/current_countries.html",
        {
            "number_of_players": number_of_humans,
            "current_countries": hands[number_of_humans],
        },
    )