# Be användaren mata in födelsemånad.
# Programmet skriver ut vilken årstid användaren är född i.

månad = str(input(f"Vilken månad fyller du i? "))
if månad == "januari" or månad == "februari" or månad == "december" or månad == "Januari" or månad == "Februari" or månad == "December":
    print(f"Du är född under vintern")
elif månad == "mars" or månad == "Mars" or månad == "april" or månad == "April" or månad == "maj" or månad == "Maj":
    print(f"Du är född under våren")
elif månad == "juni" or månad == "Juni" or månad == "juli" or månad == "Juli" or månad == "augusti" or månad == "Augusti":
    print(f"Du är född under sommaren")
elif månad == "september" or månad == "September" or månad == "oktober" or månad == "Oktober" or månad == "november" or månad == "November":
    print(f"Du är född under hösten")
else:
    print(f"Detta är inte en månad")