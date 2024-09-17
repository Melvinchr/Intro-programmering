# Be användaren mata in tre tal
# Programmet skriver ut de tre talen i storleksordning. Det minsta kommer först.

tal1 = int(input(f"Mata in första talet "))
tal2 = int(input(f"Mata in andra talet "))
tal3 = int(input(f"Mata in tredje talet "))
if (tal2 > tal1 and tal2 < tal3):
    print(f"{tal1} {tal2} {tal3}")   
elif (tal1 > tal2 and tal1 < tal3):
    print(f"{tal2} {tal1} {tal3}")
elif (tal2 > tal3 and tal2 < tal1):
    print(f"{tal3} {tal2} {tal1}")
elif (tal3 > tal1 and tal3 < tal2):
    print(f"{tal1} {tal3} {tal2}")