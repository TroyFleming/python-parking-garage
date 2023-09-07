class parkingGarage():
    '''
    This parking garage ticketing system assigns a ticket and parking space base on
    entered license plate info. A dictionary is created within currentTicket for each
    license plate entered, storing ticket number, parking space number, and paid status.

    There are a limited number of spaces (10 total), of which a corresponding ticket is assigned to.
    As customers park in the garage, the corresponding ticket and space are removed from their respective
    lists.

    If a customer pays for their parking, the ticket and space are placed back into their respective lists.
    
    If all spaces are taken, customer is notified that there are no parking spaces left in garage.
    '''
    
    def __init__(self, tickets = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'], \
                 parkingSpaces = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10'], \
                 currentTicket = {}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    # When a customer arrives to park    
    def takeTicket(self):
        # If the garage is full, customer is notified
        if len(self.tickets) == 0 or len(self.parkingSpaces) == 0:
            print('\nThe parking garage is currently full. Please try again later.')
            exit

        # If the garage is not full, asks for customers information to assign ticket and space
        else:

            # Collects license plate number to place into currentTickets dictionary
            licensePlate = input('\nPlease enter your license plate number:\n')

            # If license plate is already in system and upaid, informs customer, otherwise will add new item or update current item
            # to currentTickets dictionary
            if licensePlate in self.currentTicket or licensePlate in self.currentTicket \
                and self.currentTicket[licensePlate]['Paid'] == False:
                print('\nA ticket has already been assigned to this license plate. Please pay if you are ready to leave.')
                exit

            # If new license plate entered, collects it and creates a dictionary item to store assigned ticket number, parking space,
            # and payment status
            else:
                self.currentTicket[licensePlate.lower()] = {'Ticket': self.tickets[0], \
                                                            'Parking Space': self.parkingSpaces[0], \
                                                            'Paid': False}

                # Assigns the first available ticket and space from each list, and pops them as they are assigned
                self.tickets.pop(0)
                self.parkingSpaces.pop(0)

                yourTicket = self.currentTicket[licensePlate.lower()]['Ticket']
                yourSpace = self.currentTicket[licensePlate.lower()]['Parking Space']

                # Prints the assigned ticket number and assigned parking space for customer
                print('\nThank you! Your ticket number is: ' + str(yourTicket) + '.')
                print('Proceed to parking space: ' + str(yourSpace) + '.\n')

                # Left in to show remaining items in lists/dictionary
                print(self.tickets)
                print(self.parkingSpaces)
                print(self.currentTicket)

    # When a customer is ready to pay and leave       
    def payForParking(self):

        # Customer must enter license plate number to continue
        payPrompt = input('\nPlease enter your license plate number to pay, or type "Exit" to quit.\n\n')
        if payPrompt == 'Exit':
            exit

        # If the license plate entered is not found in dictionary currentTickets, prompts them to verify and try again
        elif payPrompt.lower() not in self.currentTicket:
            print('\nThat license plate cannot be found. Please verify the correct plate info and try again.')

        elif self.currentTicket[payPrompt.lower()]['Paid'] == True:
            print('\nThat ticket has already been paid! Please get a new ticket if you would like to use the garage.')

        # If license plate is found, prompts them for a payment type
        else:
            payOptions = input('\nYour balance is: $5.00\n\nHow would you like to pay?\n\n- Cash (Enter 1)\n- Card (Enter 2)\n ')

            # If nothing entered, or invalid options entered, goes back to main menu options
            if payOptions == '':
                exit
            
            # If either payment option is selected, pays ticket and informs them of time to leave
            elif payOptions == '1' or payOptions == '2':
                print('Your parking ticket has been paid! You have 15 minutes to exit the garage.\n\nThank you! Have a nice day.\n')

                # Once paid, returns the ticket number and parking space back to their respective lists via append
                # and changes their payment status to True
                self.tickets.append(self.currentTicket[payPrompt.lower()]['Ticket'])
                self.parkingSpaces.append(self.currentTicket[payPrompt.lower()]['Parking Space'])
                self.currentTicket[payPrompt.lower()]['Paid'] = True

                # Left in to show remaining items in lists/dictionary
                print(self.tickets)
                print(self.parkingSpaces)
                print(self.currentTicket)

findParking = parkingGarage()

def runPG():
    while True:

        # Customer must either get a new ticket, pay for a current ticket, or quit
        ticketDispense = (input('\nWhat would you like to do?\n\n- Get Ticket (Enter 1)\n- Pay (Enter 2)\n- Quit (Enter 3)\n'))

        # If option 3 (quit) entered, or left blank, quits program
        if ticketDispense == '3' or ticketDispense == '':
            break

        # If option 1 (get ticket) selected, calls takeTicket method
        elif ticketDispense == '1':
            findParking.takeTicket()

        # if option 2 (pay ticket) selected, calls payForParking method)
        elif ticketDispense == '2':
            findParking.payForParking()

runPG()

