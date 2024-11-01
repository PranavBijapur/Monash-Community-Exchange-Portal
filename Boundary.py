class Boundary:


    def __init__(self):
        pass

    def display_welcome_message(self):
        """
        displays welcome message for the user.
        :return:
        """
        print("**********************")
        print("Welcome to M.C.E.S SYSTEM")
        print("**********************")
        user_input = input("Enter 1 to Sign-up \nEnter 2 to Log-in \nEnter Q to exit\n")
        return user_input

    def display_main_menu(self):
        """
        displays the main menu and takes the user input.
        :return: string
        """
        print("**********************")
        print("Welcome to M.C.E.S SYSTEM")
        print("**********************")
        user_input = input("Enter 1 to Post an Ad\nEnter 2 to Browse Ads\nEnter 3 for Previously Posted Ads"
                           "\nEnter 4 for"
                           " Watchlist\nEnter 5 for Recently viewed Ads\nEnter 6 to log-out\n")
        return user_input

    def display_log_in(self):
        """
        displays the login for the user and takes user input.
        :return: string
        """
        print("**********************")
        print("Welcome to M.C.E.S SYSTEM")
        print("**********************")
        user_email = input("Enter email :")
        user_password = input("Enter password:")
        return user_email, user_password

    def recently_viewed_ads_display(self):
        """
        displays the recently viewed ads to the user.
        :return:
        """
        print("M.C.E.S")
        user_input = input("Recently Viewed Ads :\n Enter 1 for last hour\n Enter 2 for last day\n Enter 3 for "
                           "last 3 days")
        user_input = int(user_input)
        while user_input < 4:
            if user_input == 1:
                print("This feature is not available at the moment.")

            elif user_input == 2:
                print("This feature is not available at the moment.")

            elif user_input == 3:
                print("Ads viewed in the last 3 days is:")

