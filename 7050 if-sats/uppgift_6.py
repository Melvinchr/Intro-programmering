tal1 = int(input(f"Mata in första talet "))
tal2 = int(input(f"Mata in andra talet "))
tal3 = int(input(f"Mata in tredje talet "))
if tal2 < tal1 tal1 > tal3:
    print(f"{tal1} är minst")   
elif tal1 > tal2 < tal3:
    print(f"{tal2} är minst")
else:
    print(f"{tal3} är minst")
