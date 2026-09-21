brukernavn = "erlber"
passord = "qwerty123456!"

def login():
    b = input("brukernavn: ")
    p = input("passord: ")
    if b == brukernavn and p == passord:
        print("du har logget inn...")
        return True
    else:
        print("du har tastet feil brukernavn eller passord")
        return False

def vis_startmeny():
    print("\n=== STARTMENY ===")
    print("1) Logg inn")
    print("2) Registrer ny bruker")
    print("3) Avslutt")
    valg = input("Hva ønsker du å gjøre? ")

    if valg == "1":
        if login():
            return "innlogget"
        else:
            return "start"

    elif valg == "2":
        #logikk for registrere ny bruker
        return "start"

    elif valg == "3":
        return "quit"

    else:
        print("ugyldig valg, velg ett nymmer fra menyen")
        return "start"


def vis_innlogget_meny():
    print("\n=== MENY(innlogget) ===")
    print("1) fortell en random vits")
    print("2) Logg ut")
    print("3) avslutt")
    valg = input("Hva ønsker du å gjøre? ")

    if valg == "1":
        #logikk for å fortelle en random vits
        return "innlogget"

    elif valg == "2":
        print("du er nå logget ut....")
        return "start"

    elif valg == "3":
        return "quit"

    else:
        print("ugyldig valg, velg ett nymmer fra menyen")
        return "innlogget"

def main():
    state = "start"
    while state != "quit":
        if state == "start":
            state = vis_startmeny()
        elif state == "innlogget":
            state = vis_innlogget_meny()

main()