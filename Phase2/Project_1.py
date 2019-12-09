import sqlite3

db_connection = None # connection to the database, empty for now
db_name = "Poke.db" # exact path to database
option = 50
sTable = "Stat"
sStat = "s_hp"
sId = "s_pkid"
sFind = 0
USER = "a"
PASSWORD = "a"

try:
    db_connection = sqlite3.connect(db_name)
except sqlite3.Error as err:
    print(err)

#Search Functions
#search by ID
def pokemonID_Search():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        pkID = raw_input("\nEnter Pokemon ID: \n")
        query = ("SELECT * FROM Pokemon WHERE pk_pkid = " + pkID)
        db_curs.execute(query)
        pkIDResult = db_curs.fetchall()
        formatted_row = '{:<1} {:<12} {:<10} {:<10} {:<9}'
        print(formatted_row.format("ID", "Evolutions", "Type 1", "Type 2", "Name"))
        print("---------------------------------------------------")
        for row in pkIDResult:
            print(formatted_row.format(*row))
#Search by name
def pokemonName_Search():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        pkName = raw_input("\nEnter Pokemon Name: \n")
        query = ("SELECT * FROM Pokemon WHERE pk_name like '%" + pkName + "%'")
        db_curs.execute(query)
        pkNameResult = db_curs.fetchall()
        formatted_row = '{:<5} {:<12} {:<10} {:<10} {:<9}'
        print(formatted_row.format("ID", "Evolutions", "Type 1", "Type 2", "Name"))
        print("---------------------------------------------------")
        for row in pkNameResult:
            print(formatted_row.format(*row))

def pokemonType_Search():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        if (option == 1.31):
            pkType1 = raw_input("\nEnter Pokemon Type: \n")
            query = ("SELECT * FROM Pokemon WHERE pk_type1 like '%" + pkType1 + "%' OR pk_type2 like '%" + pkType1 + "%'")
        if (option == 1.32):
            pkType1 = raw_input("\nEnter Pokemon Type 1: \n")
            pkType2 = raw_input("\nEnter Pokemon Type 2: \n")
            query = ("SELECT * FROM Pokemon WHERE pk_type1 like '%" + pkType1 + "%' AND pk_type2 like '%" + pkType2 + "%'")
        db_curs.execute(query)
        pkTypeDuoResult = db_curs.fetchall()
        formatted_row = '{:<5} {:<12} {:<10} {:<10} {:<9}'
        print(formatted_row.format("ID", "Evolutions", "Type 1", "Type 2", "Name"))
        print("---------------------------------------------------")
        for row in pkTypeDuoResult:
            print(formatted_row.format(*row))

def pokemonEvo_Search():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        pkEvo = raw_input("\nEnter # of Pokemon Evolutions: \n")
        query = ("SELECT * FROM Pokemon WHERE pk_evo = " + pkEvo)
        db_curs.execute(query)
        pkEvoResult = db_curs.fetchall()
        formatted_row = '{:<5} {:<12} {:<10} {:<10} {:<9}'
        print(formatted_row.format("ID", "Evolutions", "Type 1", "Type 2", "Name"))
        print("---------------------------------------------------")
        for row in pkEvoResult:
            print(formatted_row.format(*row))			

def pokemonStat_Search():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()

        if (sFind == 1):
            query = ("SELECT pk_pkid, pk_evo, pk_type1, pk_type2, pk_name, " + sStat + " FROM Pokemon, " + sTable + " WHERE pk_pkid = " + sId + " AND " + sStat + " = (SELECT MIN(" + sStat + ") FROM " + sTable + ")")
        if (sFind == 2):
            query = ("SELECT pk_pkid, pk_evo, pk_type1, pk_type2, pk_name, " + sStat + " FROM Pokemon, " + sTable + " WHERE pk_pkid = " + sId + " AND " + sStat + " = (SELECT MAX(" + sStat + ") FROM " + sTable + ")")

        db_curs.execute(query)
        pkStatResult = db_curs.fetchall()
        formatted_row = '{:<5} {:<12} {:<10} {:<10} {:<9} {:<5}'
        print(formatted_row.format("ID", "Evolutions", "Type 1", "Type 2", "Name", "Stat Chosen"))
        print("---------------------------------------------------------------")
        for row in pkStatResult:
            print(formatted_row.format(*row))

def partycheck():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        partyID = raw_input("What party would you like to check: \n")
        query = ("SELECT * FROM Party WHERE pt_ptid = " + partyID)
        db_curs.execute(query)
        partyResult = db_curs.fetchall()
        formatted_row = '{:<5} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'
        print(formatted_row.format("ID", "Slot 1", "Nature 1", "Slot 2", "Nature 2", "Slot 3", "Nature 3", "Slot 4", "Nature 4", "Slot 5", "Nature 5", "Slot 6", "Nature 6"))
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for row in partyResult:
            print(formatted_row.format(*row))

#Insert Functions
def pokemon_Insert():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        pkid = raw_input("ID: \n")
        evo = raw_input("Evolutions: \n")
        type1 = raw_input("Type 1: \n")
        type2 = raw_input("Type 2: \n")
        name = raw_input("Name: \n")
        query = ("INSERT INTO Pokemon VALUES ('" + pkid + "', '" + evo + "', '" + type1 + "', '" + type2 + "', '" + name +"')" )
        db_curs.execute(query)
        #db_connection.commit()
        query1 = ("SELECT * FROM Pokemon WHERE pk_pkid = " + pkid)
        db_curs.execute(query1)
        updatedResult = db_curs.fetchall()
        formatted_row = '{:<1} {:<12} {:<10} {:<10} {:<9}'
        print(formatted_row.format("ID", "Evolutions", "Type 1", "Type 2", "Name"))
        print("---------------------------------------------------")
        for row in updatedResult:
            print(formatted_row.format(*row))

def pokeParty_Insert():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        partyNumber = raw_input("\nEnter the party #: \n")
        query = ("INSERT INTO Party  VALUES (" + partyNumber + ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ) ")
        db_curs.execute(query)
        query2 = ("SELECT * FROM Party WHERE pt_ptid = " + partyNumber)
        db_curs.execute(query2)
        pkEvoResult = db_curs.fetchall()
        formatted_row = '{:<10} {:<12} {:<10} {:<10} {:<9} {:<9} {:<9}'
        print(formatted_row.format("Party#", "Slot1", " Slot2", "Slot3", "slot4", "Slot5", "Slot6"))
        print("---------------------------------------------------")
        for row in pkEvoResult:
            print(formatted_row.format(*row))

#Delete Functions
def pokeParty_Delete():
    with sqlite3.connect("Poke.db") as db:
        #db.text_facotry = str
        db_curs = db.cursor()
        partyNumber = raw_input("\nWhich party would you like to delete: \n")
        query = ("DELETE FROM Party WHERE pt_ptid = " + partyNumber)
        db_curs.execute(query)
        print("\nParty " + partyNumber + " has been deleted\n")

def pokeDex_Delete():
    with sqlite3.connect("Poke.db") as db:
        db_curs = db.cursor()
        pokeID = raw_input("\nWhich Pokemon will you delete: \n")
        query = ("DELETE FROM Pokemon WHERE pk_pkid = " + pokeID)
        db_curs.execute(query)
        print("\nPokemon " + pokeID + " has been deleted\n")

#Update Functions
def pokeParty_Update():
	with sqlite3.connect("Poke.db") as db:
		db.text_factory = str
		db_curs = db.cursor ()
		partyNumber = raw_input("\nWhich party would you like to update: \n")
		slot1 = raw_input("\nWhat pokemon do you want for slot 1 (ID #): \n")
		slot2 = raw_input("\nWhat pokemon do you want for slot 2 (ID #): \n")
		slot3 = raw_input("\nWhat pokemon do you want for slot 3 (ID #): \n")
		slot4 = raw_input("\nWhat pokemon do you want for slot 4 (ID #): \n")
		slot5 = raw_input("\nWhat pokemon do you want for slot 5 (ID #): \n")
		slot6 = raw_input("\nWhat pokemon do you want for slot 6 (ID #): \n")
		query = ("UPDATE Party SET pt_slot1 = " + slot1 + ", pt_slot2 = " + slot2 + ", pt_slot3 = " + slot3 + ", pt_slot4 = " + slot4 + ", pt_slot5 = " + slot5 + ", pt_slot6 ='" + slot6 +  " WHERE pt_ptid = " + partyNumber)
        db_curs.execute(query)
        pokePartyResult = db_curs.fetchball()
        formatted_row = '{:<10} {:<12} {:<10} {:<10} {:<9} {:<9} {:<9} {:<12} {:<10} {:<10} {:<9} {:<9} {:<9}'
        print(formatted_row.format("Party#", "Slot1", " Slot2", "Slot3", "slot4", "Slot5", "Slot6"))
        print("---------------------------------------------------")
        for row in pokePartyResult:
            print(formatted_row.format(*row))

def pokeParty_Update1():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        partyNumber = raw_input("\nParty Number: \n")
        slotNum = raw_input("\nWhich slot: \n")
        pokeID = raw_input("\nWhich Pokemon: \n")
        query = ("UPDATE Party SET pt_slot" + slotNum + " = " + pokeID + " WHERE pt_ptid = " + partyNumber)
        db_curs.execute(query)
        query2 = ("SELECT * FROM Party WHERE pt_ptid = " + partyNumber)
        db_curs.execute(query2)
        pkPartyResult = db_curs.fetchall()
        formatted_row = '{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'
        print(formatted_row.format("Party ID", "Slot 1", "Nature 1", "Slot 2", "Nature 2", "Slot 3", "Nature 3", "Slot 4", "Nature 4", "Slot 5", "Nature 5", "Slot 6", "Nature 6"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for row in pkPartyResult:
            print(formatted_row.format(*row))

def pokemon_Update():
    with sqlite3.connect("Poke.db") as db:
        db.text_factory = str
        db_curs = db.cursor()
        pkid = raw_input("ID: \n")
        evo = raw_input("Evolutions: \n")
        type1 = raw_input("Type 1: \n")
        type2 = raw_input("Type 2: \n")
        name = raw_input("Name: \n")
        query = ("UPDATE Pokemon SET pk_evo = " + evo + ", pk_type1 = '" + type1 + "', pk_type2 = '" + type2 + "', pk_name = '" + name + "' WHERE pk_pkid = " + pkid)
        db_curs.execute(query)
        print("Pokemon Updated!")
        query1 = ("SELECT * FROM Pokemon WHERE pk_pkid = " + pkid)
        db_curs.execute(query1)
        updatedResult = db_curs.fetchall()
        formatted_row = '{:<1} {:<12} {:<10} {:<10} {:<9}'
        print(formatted_row.format("ID", "Evolutions", "Type 1", "Type 2", "Name"))
        print("---------------------------------------------------")
        for row in updatedResult:
            print(formatted_row.format(*row))

print("\nWelcome to Project Mew Database, please enter an item to execute. \n")
if option == 50:
    whatuser = input("1 - User\n2 - Admin\n")
#User
    if (whatuser == 1 ):
        option = input("\n1 - Search Pokedex\n2 - Access Party\n")
#Pokedex        
        if (option == 1):
            option = input("\nSelect how to search\n1.1 - By ID\n1.2 - By Name\n1.3 - By Type\n1.4 - By # of Evolutions\n1.5 - By Stat\n")
        if (option == 1.1):
            pokemonID_Search()
        if (option == 1.2):
            pokemonName_Search()
        if (option == 1.3):
            option = input("\nSelect what to do\n1.31 - Single Type Search\n1.32 - Duo Type Search\n")
            if (option == 1.31):
                pokemonType_Search()
            if (option == 1.32):
                pokemonType_Search()
        if (option == 1.4):
            pokemonEvo_Search()
        if (option == 1.5):
            option = input("\nSelect what to do\n1.51 - Base Stat Search\n1.52 - Min Stat Search\n1.53 - Max Stat Search\n")
            if (option == 1.51):
                sTable = "Stat"
                sId = "s_pkid"
                option = input("\nSelect what to search\n1.511 - HP\n1.512 - ATK\n1.513 - DEF\n1.514 - S-ATK\n1.515 - S-DEF\n1.516 - Speed\n1.517 - Base Stat Total\nAlso, choose 1.51_1 for Lowest, 1.51_2 for Highest\n")
                if (option >= 1.511):
                    sStat = "s_hp"
                    if (option == 1.5111):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5112):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.512):
                    sStat = "s_atk"
                    if (option == 1.5121):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5122):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.513):
                    sStat = "s_def"
                    if (option == 1.5131):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5132):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.514):
                    sStat = "s_satk"
                    if (option == 1.5141):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5142):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.515):
                    sStat = "s_sdef"
                    if (option == 1.5151):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5152):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.516):
                    sStat = "s_spd"
                    if (option == 1.5161):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5162):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.517):
                    sStat = "s_bst"
                    if (option == 1.5171):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5172):
                        sFind = 2
                        pokemonStat_Search()
            if (option == 1.52):
                sTable = "Min"
                sId = "mn_pkid"
                option = input("\nSelect what to search\n1.521 - HP\n1.522 - ATK\n1.523 - DEF\n1.524 - S-ATK\n1.525 - S-DEF\n1.526 - Speed\n1.527 - Min Stat Total\nFinally, choose 1.52_1 for Lowest, 1.52_2 for Highest\n")
                if (option >= 1.521):
                    sStat = "mn_hp"
                    if (option == 1.5211):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5212):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.522):
                    sStat = "mn_atk"
                    if (option == 1.5221):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5222):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.523):
                    sStat = "mn_def"
                    if (option == 1.5231):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5232):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.524):
                    sStat = "mn_satk"
                    if (option == 1.5241):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5242):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.525):
                    sStat = "mn_sdef"
                    if (option == 1.5251):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5252):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.526):
                    sStat = "mn_spd"
                    if (option == 1.5261):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5262):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.527):
                    sStat = "mn_mnst"
                    if (option == 1.5271):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5272):
                        sFind = 2
                        pokemonStat_Search()
            if (option == 1.53):
                sTable = "Max"
                sId = "mx_pkid"
                option = input("\nSelect what to search\n1.531 - HP\n1.532 - ATK\n1.533 - DEF\n1.534 - S-ATK\n1.535 - S-DEF\n1.536 - Speed\n1.537 - Max Stat Total\nFinally, choose 1.53_1 for Lowest, 1.53_2 for Highest\n")
                if (option >= 1.531):
                    sStat = "mx_hp"
                    if (option == 1.5311):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5312):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.532):
                    sStat = "mx_atk"
                    if (option == 1.5321):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5322):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.533):
                    sStat = "mx_def"
                    if (option == 1.5331):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5332):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.534):
                    sStat = "mx_satk"
                    if (option == 1.5341):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5342):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.535):
                    sStat = "mx_sdef"
                    if (option == 1.5351):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5352):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.536):
                    sStat = "mx_spd"
                    if (option == 1.5361):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5362):
                        sFind = 2
                        pokemonStat_Search()
                if (option >= 1.537):
                    sStat = "mx_mxst"
                    if (option == 1.5371):
                        sFind = 1
                        pokemonStat_Search()
                    if (option == 1.5372):
                        sFind = 2
                        pokemonStat_Search()
 
 #Party       
        if (option == 2):
            party = input("\n1 - Check Party\n2 - Insert Party\n3 - Change Party\n4 - Delete Party\n")
            if (party == 1):
                partycheck()
            if (party == 2):
                pokeParty_Insert()
            if (party == 3):
                pokeParty_Update1()
            if (party == 4):
                pokeParty_Delete()
#Admin
    if (whatuser == 2):
        USER1 = raw_input("\nUser Name: \n")
        PASSWORD1 = raw_input("\nPassword: \n")
        if (USER == USER1 and PASSWORD == PASSWORD1):
            print("\nHello aaaaa")
            admin = input("1 - Pokedex Update\n2 - Pokedex Insert\n3 - Pokedex Delete\n")
            if (admin == 1):
                pokemon_Update()
            if (admin == 2):
                pokemon_Insert()
            if (admin == 3):
                pokeDex_Delete()
