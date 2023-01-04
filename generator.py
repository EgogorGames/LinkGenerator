import requests
import time
import os
DC = '\033[36m'
B = '\033[94m'
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
BOLD = '\033[1m'
lan = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']
v_lnk = []
fail = right = gen = 0
print(f"{B}{G}#################################")
print("#                               #")
print("#  L i n k s G e n e r a t o r  #")
print("#                               #")
print("#   ©EgogorGames 2022 - 2023    #")
print("#                               #")
print("#################################")
print(f"{Y}---------------Note:-------------")
print("Please use this app only in web programming or other good things; don't use it for hacking secret links, etc.")
print("If you send many requests on the web page and it is for 1 - 10 minutes links not generates maybe your IP is banned for some time or forever on this web page!")
print("The generator is buggy, so if you find an error you can write to us on my discord account: KartoshkaDobriy#7031")
print(f"{DC}---------------Setup-------------")
link = str(input("Input a link: "))
c_len = int(input("Input how many charters in your code(Maximum 10): "))
gen_count = str(input("Input how many links to generate(Optional): "))
gen_start = str(input("Input how many links I need to skip(Optional): "))
print("--------------LOADING-------------")
if gen_count == "" or gen_count == " ":
    gen_count = 0
else:
    gen_count = int(gen_count)
if gen_start == "" or gen_start == " ":
    gen_start = 0
else:
    gen_start = int(gen_start)
def generate(code : str):
    global v_lnk
    global fail
    global right
    global gen
    try:
        if gen >= gen_start:
            if link[len(link) - 1] == "/":
                lnk = f"{link}/{code}"
            else:
                lnk = f"{link}/{code}"
            req = requests.get(lnk)
            if req.status_code == 429:
                v_lnk.append(lnk)
                print("!!! WAIT 30 SECONDS, WE MAY BE BLOCKED !!!")
                print("# If after 1 - 10 minutes nothing is generated that means that your IP banned for some time or forever!")
                print("# (You can try to run this script on another computer with some skipped generations!)")
                time.sleep(30)
            else:
                gen = gen + 1
                if req.status_code != 404:
                    v_lnk.append(lnk + f" {gen}")
                    right = right + 1
                else:
                    fail = fail + 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("------------------------")
                print("Links found:")
                print("link--------------num---")
                for vlink in v_lnk:
                    print(vlink)
                print("------------------------")
                print("Last generated link: " + lnk)
                print("------------------------")
                print("Not working links: " + str(fail))
                print("Working links: " + str(right))
                print("Generated links: " + str(gen))
                print("------------------------")
        else:
            gen = gen + 1
    except:
        print(f"{R}ERORR{DC}")
if c_len == 1:
    for l1 in lan:
        if int(gen_count + gen_start) <= int(gen):
            break
        code = l1
        generate(code)
elif c_len == 2:
    for l1 in lan:
        for l2 in lan:
            if int(gen_count + gen_start) <= int(gen):
                break
            code = l1 + l2
            generate(code)
elif c_len == 3:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                if int(gen_count + gen_start) <= int(gen):
                    break
                code = l1 + l2 + l3
                generate(code)
elif c_len == 4:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                for l4 in lan:
                    if int(gen_count + gen_start) <= int(gen):
                        break
                    code = l1 + l2 + l3 + l4
                    generate(code)
elif c_len == 5:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                for l4 in lan:
                    for l5 in lan:
                        if int(gen_count + gen_start) <= int(gen):
                            break
                        code = l1 + l2 + l3 + l4 + l5
                        generate(code)
elif c_len == 6:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                for l4 in lan:
                    for l5 in lan:
                        for l6 in lan:
                            if int(gen_count + gen_start) <= int(gen):
                                break
                            code = l1 + l2 + l3 + l4 + l5 + l6
                            generate(code)
elif c_len == 7:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                for l4 in lan:
                    for l5 in lan:
                        for l6 in lan:
                            for l7 in lan:
                                if int(gen_count + gen_start) <= int(gen):
                                    break
                                code = l1 + l2 + l3 + l4 + l5 + l6 + l7
                                generate(code)
elif c_len == 8:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                for l4 in lan:
                    for l5 in lan:
                        for l6 in lan:
                            for l7 in lan:
                                for l8 in lan:
                                    if int(gen_count + gen_start) <= int(gen):
                                        break
                                    code = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8
                                    generate(code)
elif c_len == 9:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                for l4 in lan:
                    for l5 in lan:
                        for l6 in lan:
                            for l7 in lan:
                                for l8 in lan:
                                    for l9 in lan:
                                        if int(gen_count + gen_start) <= int(gen):
                                            break
                                        code = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
                                        generate(code)
elif c_len == 10:
    for l1 in lan:
        for l2 in lan:
            for l3 in lan:
                for l4 in lan:
                    for l5 in lan:
                        for l6 in lan:
                            for l7 in lan:
                                for l8 in lan:
                                    for l9 in lan:
                                        for l10 in lan:
                                            if int(gen_count + gen_start) <= int(gen):
                                                break
                                            code = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10
                                            generate(code)
else:
    print("Not right code char count!")
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{Y}---------Statistic---------")
print("Number of links created: " + gen_count)
print("")
print("Generated links: " + str(gen))
print("Not working links: " + str(fail))
print("Working links " + str(right))
print("--------Links found-------")
for vlink in v_lnk:
    print("- " + vlink)
print("---------------------------")