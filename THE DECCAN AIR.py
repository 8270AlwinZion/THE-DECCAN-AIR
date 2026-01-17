passengers = []
while True:
    print("\nWELCOME TO DECCANAIR ✈️")
    print("\nJoy Of Flying")
    print("1. View Available Flights✈")
    print("2. Ticket Booking 🎫")
    print("3. In-Flight Beverages 🍇")
    print("4. Car Parking Spot Reservation 🚗")
    print("5. About Us 👥")
    print("6. Quit 📤")

    choice = int(input("\nEnter your choice from 1-6: "))

    # ==================== VIEW AVAILABLE FLIGHTS ====================
    # =====================SURYA PRAKASH==============================
    if choice == 1:
        passengers = []
        od = input("Enter the type (international/domestic): ").lower()

        # ================= INTERNATIONAL =================
        if od == "international":
            menu = ["malayisa", "thailand", "singapore", "srilanka", "america", "england"]
            menu2 = ["chennai", "delhi", "orissa", "ahemedabadh", "hyderabad"]

            print("\nArrival menu:", menu)
            print("Departure menu:", menu2)

            while True:
                depature = input("\nEnter your departure from menu2: ").lower()
                arrival = input("Enter your arrival from menu: ").lower()

                if depature not in menu2:
                    print("❌ Departure not available, try again")
                elif arrival not in menu:
                    print("❌ Arrival not available, try again")
                else:
                    if arrival == "malayisa":
                        print("Air India flight available")
                    elif arrival == "thailand":
                        print("Air Asia flight available")
                    elif arrival == "singapore":
                        print("Indigo flight available")
                    elif arrival == "srilanka":
                        print("Air India flight available")
                    elif arrival == "america":
                        print("Kingfisher flight available")
                    elif arrival == "england":
                        print("England Airlines flight available")

                    passengers.append({
                        "Departure": depature,
                        "Arrival": arrival
                    })
                    break

        # ================= DOMESTIC =================
        elif od == "domestic":
            depature_menu = ["chennai", "andhrapradesh", "delhi", "mumbai", "bengaluru", "kolkata"]
            arrival_menu = ["chennai", "delhi", "orisa", "ahemedabadh", "hyderabad",
                            "andhrapradesh", "mumbai", "bengaluru", "kolkata"]

            print("\nDeparture menu:", depature_menu)
            print("Arrival menu:", arrival_menu)

            while True:
                depature = input("\nEnter your departure from depature_menu: ").lower()
                arrival = input("Enter your arrival from arrival_menu: ").lower()

                if depature not in depature_menu:
                    print("❌ Departure not available, try again")
                elif arrival not in arrival_menu:
                    print("❌ Arrival not available, try again")
                else:
                    if arrival == "chennai":
                        print("Air India flight available")
                    elif arrival == "delhi":
                        print("Air Asia flight available")
                    elif arrival == "orisa":
                        print("Indigo flight available")
                    elif arrival == "ahemedabadh":
                        print("Air India flight available")
                    elif arrival == "mumbai":
                        print("Kingfisher flight available")
                    elif arrival == "hyderabad":
                        print("Indian Airlines flight available")
                    elif arrival == "andhrapradesh":
                        print("Air India flight available")
                    elif arrival == "bengaluru":
                        print("Air Asia flight available")
                    elif arrival == "kolkata":
                        print("Indigo flight available")

                    passengers.append({
                        "Departure": depature,
                        "Arrival": arrival
                    })
                    break

        else:
            print("❌ Invalid type entered")

    # ==================== TICKET BOOKING ====================
    # ====================THARAK==============================
    elif choice == 2:
        passengers = []

        # First passenger details
        name = input("\nEnter your name: ")
        age = int(input("Enter your age: "))
        phone = input("Enter your phone number: ")
        aadhar = input("Enter your Aadhar ID: ")
        email = input("Enter your mail ID: ")

        passengers.append({
            "Name": name,
            "Age": age,
            "Phone": phone,
            "Aadhar": aadhar,
            "Email": email
        })

        print("\n✅ Your details are saved successfully")
        print("\nDomestic Package : ₹12,000")
        print("International Package : ₹80,000")

        while True:
            Intdo = input("\nChoose Flight Type (Domestic/International): ").capitalize()
            if Intdo == "International":
                print("\nAvailable Countries:")
                print("Singapore, Malaysia, Sri Lanka, Pakistan, United States, South Korea")
                break
            elif Intdo == "Domestic":
                print("\nAvailable States:")
                print("Tamil Nadu, Karnataka, Kerala, Andhra Pradesh, Delhi, Mumbai, Odisha")
                break
            else:
                print("❌ Not valid. Please enter again.")

        From = input("\nEnter your departure location: ")
        To = input("Enter your arrival location: ")

        # Additional passengers
        while True:
            per = input("\nAdd another person? (Yes/No): ").lower()
            if per == "yes":
                new_passenger = {
                    "Name": input("Enter new passenger name: "),
                    "Age": int(input("Enter age: ")),
                    "Phone": input("Enter phone number: "),
                    "Aadhar": input("Enter Aadhar ID: "),
                    "Email": input("Enter mail ID: ")
                }
                passengers.append(new_passenger)
            elif per == "no":
                break
            else:
                print("❌ Please enter Yes or No.")

        # Fare calculation
        Pers = len(passengers)
        fare = Pers * 80000 if Intdo == "International" else Pers * 12000

        Payment = input("\nEnter the receipt ID: ")

        # Ticket summary
        print("\n📄 TICKET DETAILS")
        print("----------------------------")
        print("Flight Type :", Intdo)
        print("Departure   :", From)
        print("Arrival     :", To)
        print("Passengers  :", Pers)
        print("Total Fare  : ₹", fare)
        print("Payment ID  :", Payment)

        print("\n👥 PASSENGER DETAILS")
        count = 1
        for p in passengers:
            print("\nPassenger", count)
            for key, value in p.items():
                print(key, ":", value)
            count += 1

        print("\n🎉 Ticket Booked Successfully!")
        print("Thank you for choosing DECCAN AIR ✈️")

    # ==================== IN-FLIGHT BEVERAGES ====================
    # =====================SURYAPRAKASH============================
    elif choice == 3:
        if not passengers:
            print("❌ No passengers booked yet! Please book a ticket first.")
            continue

        print("\n🥩 NON-VEG FOOD PACKAGE = $800")
        print("🥗 VEG FOOD PACKAGE = $500")

        food_type = input("Enter your choice (NON VEG / VEG): ").upper()

        if food_type == "NON VEG":
            NON_VEG_MENU = ["CHICKEN BRIYANI", "MUTTON BRIYANI", "TANDOORI", "LOBSTER", "GRILLED KEBABS", "BOILED EGGS"]
            print("\nAvailable NON-VEG In-Flight Beverages Menu:")
            print(", ".join(NON_VEG_MENU))

            while True:
                selected_food = input("\nEnter your choice from the NON-VEG menu: ").upper()
                if selected_food not in NON_VEG_MENU:
                    print("❌ Selected item not available, please try again")
                else:
                    print("✅ Your choice is saved successfully")
                    break

        elif food_type == "VEG":
            VEG_MENU = ["PANEER TIKKA", "VEG BRIYANI", "SALAD", "CHAPATI", "VEG NOODLES"]
            print("\nAvailable VEG In-Flight Beverages Menu:")
            print(", ".join(VEG_MENU))

            while True:
                selected_food = input("\nEnter your choice from the VEG menu: ").upper()
                if selected_food not in VEG_MENU:
                    print("❌ Selected item not available, please try again")
                else:
                    print("✅ Your choice is saved successfully")
                    break
        else:
            print("❌ Invalid choice entered!")
            continue

        num_passengers = len(passengers)
        food_fare = num_passengers * (800 if food_type == "NON VEG" else 500)

        food_payment_id = input("\nEnter the food receipt ID: ")

        print("\n📄 FOOD / IN-FLIGHT BEVERAGES DETAILS")
        print("----------------------------")
        print("Food Type       :", food_type)
        print("Selected Item   :", selected_food)
        print("Number of Orders:", num_passengers)
        print("Total Fare      : ₹", food_fare)
        print("Payment ID      :", food_payment_id)

        print("\n🎉 In-Flight Beverages Booked Successfully!")
        print("Thank you for choosing DECCAN AIRLINES✈️")
    # ==================== CAR PARKING SPOT RESERVATION ====================
    # =====================THARAK============================
    elif choice == 4:
        print("\nWELCOME TO DECCAN AIR")
        print("\nReserve your Car Parking spot")
        terminal = input("Boarding Terminal: (International / Domestic):").lower()

        # ================= INTERNATIONAL =================
        if terminal == "international":
            print("\n Welcome to International Terminal Car Parking")
            print("\n Parking Slot Available:50")
            print("Parking Spot Packages")
            print("1.One Week :  ₹800")
            print("2.One Month:  ₹3500")

            name1 = input("Name:")
            vehno = input("Vehicle Number:")
            vehtype = input("Vehicle Type(SUV / SEDAN / HATCHBACK / etc):")

            package = int(input("choose your package (1/2) :"))

            total_slot = 50
            booked_slot = 0

            if package == 1:
                n = int(input("Number of Parking spots :"))
                print("your data has been saved")

                n1 = input("would you like to proceed (Yes/No:)").lower()

                if n1 == "yes":
                    if booked_slot + n <= total_slot:
                        booked_slot += n
                        available_slots = total_slot - booked_slot
                        print("✅ Parking slot booked successfully")
                        print("Total Cost:", n * 800)
                        payy = input("enter the reciept ID:")
                        print("Thank you for Booking a Parking slot")
                        print("Available Slots:", available_slots)
                    else:
                        print("❌ Parking Full")

            elif package == 2:
                n = int(input("Number of Parking spots :"))
                print("your data has been saved")

                n1 = input("would you like to proceed (Yes/No:)").lower()

                if n1 == "yes":
                    if booked_slot + n <= total_slot:
                        booked_slot += n
                        available_slots = total_slot - booked_slot
                        print("✅ Parking slot booked successfully")
                        print("Total Cost:", n * 3500)
                        payy = input("enter the reciept ID:")
                        print("Thank you for Booking a Parking slot")
                        print("Available Slots:", available_slots)
                    else:
                        print("❌ Parking Full")
            else:
                print("Invalid package choice")

        # ================= DOMESTIC =================
        elif terminal == "domestic":
            print("\n Welcome to Domestic Terminal Car Parking")
            print("\n Parking Slot Available:70")
            print("Parking Spot Packages")
            print("1.One Week :  ₹500")
            print("2.One Month:  ₹2000")

            name1 = input("Name:")
            vehno = input("Vehicle Number:")
            vehtype = input("Vehicle Type(SUV / SEDAN / HATCHBACK / etc):")

            package = int(input("choose your package (1/2) :"))

            total_slot = 70
            booked_slot = 0

            if package == 1:
                n = int(input("Number of Parking spots :"))
                print("your data has been saved")

                n1 = input("would you like to proceed (Yes/No:)").lower()

                if n1 == "yes":
                    if booked_slot + n <= total_slot:
                        booked_slot += n
                        available_slots = total_slot - booked_slot
                        print("✅ Parking slot booked successfully")
                        print("Total Cost:", n * 500)
                        payy = input("enter the reciept ID:")
                        print("Thank you for Booking a Parking slot")
                        print("Available Slots:", available_slots)
                    else:
                        print("❌ Parking Full")

            elif package == 2:
                n = int(input("Number of Parking spots :"))
                print("your data has been saved")

                n1 = input("would you like to proceed (Yes/No:)").lower()

                if n1 == "yes":
                    if booked_slot + n <= total_slot:
                        booked_slot += n
                        available_slots = total_slot - booked_slot
                        print("✅ Parking slot booked successfully")
                        print("Total Cost:", n * 2000)
                        payy = input("enter the reciept ID:")
                        print("Thank you for Booking a Parking slot")
                        print("Available Slots:", available_slots)
                    else:
                        print("❌ Parking Full")
            else:
                print("Invalid package choice")

        else:
            print("Invalid terminal choice")
    # ==================== About Us ====================
    # =====================THARAK============================
    elif choice == 5:
        print("\nABOUT US")
        print("DECCAN AIR is a conceptual airline management system developed as a Python menu-driven application.")
        print("\n===========================================================================")
        print("The main aim of this project is to demonstrate the practical use of Python programming concepts")
        print("such as conditional statements, loops, user input handling, and basic data management.")
        print("\n===========================================================================")
        print("This application provides multiple services including flight information, ticket booking, in-flight food services, and car parking reservation")
        print("Each module is designed to simulate real-world airline operations in a simple and user-friendly manner.")
        print("\n===========================================================================")
        print("The project has been developed as part of the Computer Science curriculum to enhance logical thinking, problem-solving skills,")
        print("It also helps to understand how software solutions can be applied to real-life scenarios.")
        print("\n===========================================================================")
        print("\nThank you")
#=======================EXIT=================
        #============= tharak===================
    elif choice == 6:
        import time #TIME MODULE

        print("Exiting.")
        time.sleep(0.5)
        print("Exiting..")
        time.sleep(0.5)
        print("Exiting...")
        time.sleep(0.5)
        print("\nThank you for using DECCAN AIR ✈️")
        print("\nHave a Safe Flight")
        break
    else:
        print("\nInvalid Choice")
        print("Enter Choice from 1 TO 6")    


    
