tal = int(input("Mata in ett tal: "))
if 0 <= tal <= 9:
    print(f"{tal} är ett ensiffrigt tal")
elif 10 <= tal <= 99:
    print(f"{tal} är ett tvåsiffrigt tal")
elif 100 <= tal <= 999:
    print(f"{tal} är ett tresiffrigt tal")
elif tal >= 1000:
    print(f"{tal} är minst ett fyrasiffrigt tal")
else:
    print(f"Talet är mindre än 0")