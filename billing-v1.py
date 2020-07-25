import csv 
import names
import random
import string

name_file = input("Name this file: ")  #start of the program, naming
csv_name = name_file + ".csv"

catchall = input("Catchall format(@catchall.com): ")

main_address = input("Main address: ")
number_of_letters = int(input("3 or 4 letters for the address jig: "))
addy2 = input("Do you want to use an address line 2 jig? Ex. Unit #194 (y/n): ")

city = input("City: ")
state = input("State format(NY as New York): ")
zipcode = int(input("Zipcode: "))

i = 1 
number_of_profiles = input("How many profiles: ")
profile_base_name = input("Base name for profiles Ex. footsites, ys...: ")

with open(csv_name, "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Email Address', 'Profile Name', 'Only One Checkout', 'Name on Card', 'Card Type', 'Card Number', 'Expiration Month', 'Expiration Year', 'CVV', 'Same Billing/Shipping', 'Shipping Name', 'Shipping Phone', 'Shipping Address', 'Shipping Address 2', 'Shipping Address 3', 'Shipping Post Code', 'Shipping City', 'Shipping State', 'Shipping Country', 'Billing Name', 'Billing Phone', 'Billing Address', 'Billing Address 2', 'Billing Address 3', 'Billing Post Code', 'Billing City', 'Billing State', 'Billing Country', 'otherEntriesList', 'Size (Optional)'])

    while i <= int(number_of_profiles):
        profile_name = profile_base_name + str(i)

        print('1. AmericanExpress \n2. MasterCard \n3. Discover \n4. Visa')
        card_type = input("Card type (use the numbers): ")

        if int(card_type) == 1: 
            type_of_card = "AmericanExpress"
        elif int(card_type) == 2: 
            type_of_card = "MasterCard"
        elif int(card_type) == 3: 
            type_of_card = "Discover"
        else: 
            type_of_card = "Visa"
        
        card_number = input("Card Number: ")
        expiration_date = input("Expiration date(XX/20XX): ") 
        expiration_date_splitted = expiration_date.split('/')
        expiration_month = expiration_date_splitted[0]
        expiration_year = expiration_date_splitted[1]
        cvv = input("CVV: ")

        random_name = names.get_full_name()
        random_name_splitted = random_name.split(' ')
        together_catchall = random_name_splitted[0] + random_name_splitted[1] + catchall

        area_code = ['347', '917', '631', '718']
        def phone_number():
            random_area_code = random.choice(area_code) + str(random.randint(1111111, 9999999))

            return random_area_code

        phone = phone_number()

        line_two = ' '

        def address_two_jig():
            
            random_number_for_addy2 = random.randint(0,999)
            address_line_two = ['Unit', 'APT', 'Apartment']
            jigged2 = random.choice(address_line_two) + " #" + str(random_number_for_addy2)

            return jigged2
        
        letters = string.ascii_uppercase
        rand_letters = random.choices(letters,k=number_of_letters)

        if number_of_letters == 3:
            address_line_one = rand_letters[0] + rand_letters[1] + rand_letters[2] + " " + main_address

            if addy2 == 'y':
                line_two = address_two_jig()

        else:
            address_line_one = rand_letters[0] + rand_letters[1] + rand_letters[2] + rand_letters[3]  + " " + main_address

            if addy2 == 'y':
                line_two = address_two_jig()
        
        csv_writer.writerow([together_catchall, profile_name, 'FALSE', random_name, type_of_card, card_number, expiration_month, expiration_year, cvv, 'TRUE', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', random_name, phone, address_line_one, line_two, ' ', zipcode, city, state, 'United States', ' ', ' '])

        i += 1

csv_file.close()