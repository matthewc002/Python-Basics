
import json
import time

time.sleep(2)

#Dictionary For Data Storage


#Astronaut Data Storage Func
def collect_data():
    astronaut_name= input("What is the name of the astronaut you're logging (First/Last)?: ")
    astronaut_mission= input(f"Name of {astronaut_name}'s mission?: ")
    astronaut_years= input(f"{astronaut_name}'s years of experience?: ")
    astronaut_active= input(f"Finally, {astronaut_name}'s active status?: ")
    print('Thank you, data successfully stored. ')
    return [astronaut_name, astronaut_mission, astronaut_years, astronaut_active]


#JSON Load File Func
def load_file(filename= 'astronautlog.json'):
    try:
        with open (filename, 'r') as file:
            return (json.load(file))
    except FileNotFoundError:
        return {}
        

    
#JSON Edit File Func
def edit_log(astronautlog):
    astronaut_id= input('''Which astronaut's information would you like to edit? 
    | Astronaut 1 | Astronaut 2 | Astronaut 3 |
    \n''')
    if astronaut_id in (astronautlog):
        print(f"Editing {astronaut_id}'s data... ")
        astronautlog[astronaut_id]= collect_data()
        print(f"Astronuat {astronaut_id}'s data successfully updated")
    else:
        print("Data not found, please choose an astronaut already within the database")

#JSON View File Func
def view_log(astronautlog):
    if astronautlog:
        print("Here is the data... \n")
        print(json.dumps(astronautlog, indent=4))
    else:
        print('No data found')

#JSON Save File Func
def save_data(data, filename= 'astronautlog.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent= 4)
        print(f'Data successfuly saved to {filename}!')
    

#Main Program

def main():
        
    name=input('Hello, your name? ')
    print(f'{name}, Welcome to the Astronaut Space Logger... \n )')

    time.sleep(2)

    astronautlog= {}

    while True:

        choice= input(f'''{name}, What is on todays agenda?
        | 1. Add Data: |
        | 2. Edit Log: |
        | 3. View Log: | 
        | 'Q' to quit: |
        ''').strip().upper()

    #Add Data Func

        if choice in ('1','1.'):

            for i in range(1, 4):
                print(f"Logging Astronaut {i}'s data")
                astronautlog[f'Astronaut {i}']= collect_data()
                save_data(astronautlog)

    #Print Success
            print("Collected astronaut's data:")
            print(json.dumps(astronautlog, indent= 4))

            save_data(astronautlog)

            print(f'Thank you {name}')

        elif choice in ('2','2.'):
            print("Sure no problem... ")
            edit_log(astronautlog)
            save_data(astronautlog)

        elif choice in ('3','3.'):
            print("Great, let's see... ")
            view_log(astronautlog)

        elif choice== 'Q':
            print(f'Thank you {name}, have a great day! ')
            break
        
        else:
            print('Invalid Choice, enter again')




#Run program
if __name__== '__main__':
    main()