import random


LW = [ "Son", "Khvicha", "Raphinha", "Diaz", "Leao", "Vini Jr.", "Grealish", "Neymar Jr.", "Gnabry", "Coman"]
RW = [ "Salah", "Messi", "Sane", "Foden", "Rodrygo", "Dembele", "Yamal", "Olise", "Kulusevski", "Savinho"]
ST = [ "Gyokeres", "Marmoush", "Lewandowski", "Lautaro", "Mbappe", "Haaland", "Kane", "Cristiano", "Alvarez", "Gakpo"]
AM_DM = [ "Musiala", "Wirtz", "Rodri", "Olmo", "Casemiro", "Odegaard", "Kimmich", "Griezmann", "Dybala", "Tchouemeni"]
CM = [ "KDB", "Modric", "Valverde", "Bellingham", "Pedri", "B.Silva", "Mac-Allister", "Gavi", "Vitinha", "Goretzka", "Llorente","Bruno", "De Jong", "Calhanoglu", "Gundogan", "Soler", "Savic", "Barella", "Kovacic", "Camavinga"]
LB = [ "Robertson", "Davies", "Mendy", "Gvardiol", "Nuno", "Grimaldo", "Balde", "Theo", "Alba", "Dalot"]
RB = [ "Trent", "Walker", "Kounde", "Hakimi", "Carvajal", "James", "White", "Wan Bissaka", "Pedro Porro", "Mazraoui"]
CB = [ "VVD", "Gabriel", "Saliba", "Lisandro", "Dias", "Akanji", "Schlotterbeck", "Araujo", "Rudiger", "Militao", "Marquinhos","Cubarsi", "Kim Min Jae", "De Ligt", "Bastoni", "Skriniar", "Konate", "Hummels", "Stones", "De Vrij"]
GK = [ "Alisson", "Ederson", "Neuer", "Courtois", "Donnarumma", "Ter Stegen", "Kobel", "Maignan", "Sels", "Oblak"]

def players(mang, player):
    print("\nManagers", end="    ")
    for j in range(0,player):
        print(mang[j], end="    ")

def left_wing(lw):
    print("\n\nLW     ", end="    ")
    for _ in range(lw):
        lw_index = random.randint(0, (len(LW) - 1))
        selected_lw = LW.pop(lw_index)
        print(f"{selected_lw}", end="    ")

def right_wing(rw):
    print("\nRW     ", end="    ")
    for _ in range(rw):
        rw_index = random.randint(0, (len(RW) - 1))
        selected_rw = RW.pop(rw_index)
        print(f"{selected_rw}", end="    ")

def striker(st):
    print("\nST     ", end="    ")
    for _ in range(st):
        st_index = random.randint(0, (len(ST) - 1))
        selected_st = ST.pop(st_index)
        print(f"{selected_st}", end="    ")

def am_dm(ad):
    print("\nAM/DM  ", end="    ")
    for _ in range(ad):
        ad_index = random.randint(0, (len(AM_DM) - 1))
        selected_ad = AM_DM.pop(ad_index)
        print(f"{selected_ad}", end="    ")

def left_cm(lcm):
    print("\nLCM    ", end="    ")
    for _ in range(lcm):
        lcm_index = random.randint(0, (len(CM) - 1))
        selected_lcm = CM.pop(lcm_index)
        print(f"{selected_lcm}", end="    ")

def right_cm(rcm):
    print("\nRCM    ", end="    ")
    for _ in range(rcm):
        rcm_index = random.randint(0, (len(CM) - 1))
        selected_rcm = CM.pop(rcm_index)
        print(f"{selected_rcm}", end="    ")

def left_back(lb):
    print("\nLB     ", end="    ")
    for _ in range(lb):
        lb_index = random.randint(0, (len(LB) - 1))
        selected_lb = LB.pop(lb_index)
        print(f"{selected_lb}", end="    ")

def right_back(rb):
    print("\nRB     ", end="    ")
    for _ in range(rb):
        rb_index = random.randint(0, (len(RB) - 1))
        selected_rb = RB.pop(rb_index)
        print(f"{selected_rb}", end="    ")

def left_cb(lcb):
    print("\nLCB    ", end="    ")
    for _ in range(lcb):
        lcb_index = random.randint(0, (len(CB) - 1))
        selected_lcb = CB.pop(lcb_index)
        print(f"{selected_lcb}", end="    ")

def right_cb(rcb):
    print("\nRCB    ", end="    ")
    for _ in range(rcb):
        rcb_index = random.randint(0, (len(CB) - 1))
        selected_rcb = CB.pop(rcb_index)
        print(f"{selected_rcb}", end="    ")

def goalie(gk):
    print("\nGK     ", end="    ")
    for _ in range(gk):
        gk_index = random.randint(0, (len(GK) - 1))
        selected_gk = GK.pop(gk_index)
        print(f"{selected_gk}", end="    ")

FW = LW + RW + ST
MF = CM + AM_DM
DF = LB + RB + CB

def forwards(fw):
    print("\nFW     ", end="    ")
    for _ in range(fw):
        fw_index = random.randint(0, len(FW) - 1)
        selected_fw = FW.pop(fw_index)
        print(f"{selected_fw}", end="    ")

def midfielders(mf):
    print("\nMF     ", end="    ")
    for _ in range(mf):
        mf_index = random.randint(0, len(MF) - 1)
        selected_mf = MF.pop(mf_index)
        print(f"{selected_mf}", end="    ")

def defenders(df):
    print("\nDF     ", end="    ")
    for _ in range(df):
        df_index = random.randint(0, len(DF) - 1)
        selected_df = DF.pop(df_index)
        print(f"{selected_df}", end="    ")



users = []

while True:
    try:
        n = int(input( "How many players are playing(maximum 5)?" ))
        if (n < 5):
            break
        else:
            print("Number entered is greater than 5!  Please enter a number between 1-5.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

for i in range (1,n+1):
    user = input( f"Name of player {i} : ")
    users.append(user)


players(users, n)
left_wing(n)
right_wing(n)
striker(n)
am_dm(n)
left_cm(n)
right_cm(n)
left_back(n)
right_back(n)
left_cb(n)
right_cb(n)
goalie(n)

print("\n\nReserves")

goalie(n)
forwards(n)
forwards(n)
midfielders(n)
midfielders(n)
defenders(n)
defenders(n)


ex = input("\n\nPress Y to exit")