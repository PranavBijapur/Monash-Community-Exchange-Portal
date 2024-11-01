import datetime
from Boundary import Boundary
from Item import Item


class Control:
    """
    Attributes:
        user_choice: str value which determines the users choice to either log-in, sign-up or exit.
        user_credentials_1 : str value of user email.
        user_credentials_2: str value of user password.
        user_decision: str value of user decision in the main menu of the function.
        temp_ad : object of Item class
        boundary : object of Boundary class
        now : contains the datetime value

    Methods:
        main():
        handles the main flow of the program.

        login():
        verifies the user login details.
        :returns
        boolean

        post_ad():
        creates an ad the user wants to post

        ad_details():
        takes user input regarding the ad in creating the ad in post_ad()

        browse_ad():
        displays the ads to the user to browse

        recently_viewed_ads():
        displays  the recently viewed ads to the user on the basis of choice by the user.

        previously_posted_ad():
        displays the ads the user previously posted. Not in use.

        watchlist():
        displays ads the user has put in watchlist.Not in use.

        log_out():
        helps user to exit the system.

    """

    def __init__(self):
        """
        init function for control class.
        """
        pass

    def main(self):
        """
        controls the flow of the overall program.
        :return:
        """
        while True:
            boundary = Boundary()
            user_choice = boundary.display_welcome_message()
            if user_choice == '2':
                user_credentials_1, user_credentials_2 = boundary.display_log_in()
                login_status = self.login(user_credentials_1, user_credentials_2)
                while login_status:
                    user_decision = boundary.display_main_menu()
                    if user_decision == '1':
                        self.post_ad()
                    elif user_decision == '2':
                        self.browse_ad()
                    elif user_decision == '3':
                        self.previously_posted_ads()
                    elif user_decision == '4':
                        self.watchlist()
                    elif user_decision == '5':
                        self.recently_viewed_ads()
                    elif user_decision == '6':
                        self.log_out()
            elif user_choice == '1':
                print("This feature is not available at the moment.")
            elif user_choice == 'Q' or user_choice == 'q':
                self.log_out()

    def login(self,user_email,user_password):
        """
        checks for user details
        :param user_email:
        :param user_password:
        :return: boolean
        """
        if "@student.monash.edu" in user_email:
            print()
            if user_password == "Monash1234":
                print("Login is successful")
                return True

    def post_ad(self):
        """
        creates an ad for the user

        :return:
        """
        user_in = input("Enter 1 for Item \nEnter 2 for service\n")
        if user_in == "1":
            temp_ad = Item()
            control = Control()
            control.ad_details(temp_ad)
            item_category_detail = (input("Enter item category:\nEnter 1 for Furniture \nEnter 2 for Textbook\nEnter "
                                          "3 for Miscellaneous\n"))
            if item_category_detail == '1':
                temp_ad.set_item_category("Furniture")
                item_sub_category_detail = input("Enter item sub-category:\nEnter 1 for big furniture \nEnter 2"
                                                 " for small furniture\n")
                if item_sub_category_detail == '1':
                    temp_ad.set_item_sub_category("Big")
                elif item_sub_category_detail == '2':
                    temp_ad.set_item_sub_category("Small")
            elif item_category_detail == '2':
                temp_ad.set_item_category("Textbook")
                item_sub_category_detail = input("Enter item sub-category:\nEnter 1 for Arts\nEnter 2 for Business and"
                                                 " education\nEnter 3 for Education\nEnter 4 for Engineering\nEnter 5 "
                                                 "for Information technology\nEnter 6 for Law\nEnter 7 for"
                                                 " Medicine/Nursing\nEnter 8 for Pharmacy\n")
                if item_sub_category_detail == '1':
                    temp_ad.set_item_sub_category("Arts")
                elif item_sub_category_detail == '2':
                    temp_ad.set_item_sub_category("Business and education")
                elif item_sub_category_detail == '3':
                    temp_ad.set_item_sub_category("Education")
                elif item_sub_category_detail == '4':
                    temp_ad.set_item_sub_category("Engineering")
                elif item_sub_category_detail == '5':
                    temp_ad.set_item_sub_category("Information technology")
                elif item_sub_category_detail == '6':
                    temp_ad.set_item_sub_category("Law")
                elif item_sub_category_detail == '7':
                    temp_ad.set_item_sub_category("Medicine/Nursing")
                elif item_sub_category_detail == '8':
                    temp_ad.set_item_sub_category("Pharmacy")

            elif item_category_detail == '3':
                temp_ad.set_item_category("Miscellaneous")
            item_condition_detail = (input("Enter item condition :\nEnter 1 for new\nEnter 2 for used\n"))
            if item_condition_detail == '1':
                temp_ad.set_item_condition('New')
            else:
                temp_ad.set_item_condition('Used')
            item_trade_option = input("Enter item trade option :\nEnter 1 for Pickup On Campus\nEnter 2 for Pickup "
                                      "Off Campus\nEnter 3 for Deliver to Home\n")
            if item_trade_option == '1':
                temp_ad.set_trade_type("Pickup On Campus")
            elif item_trade_option == '2':
                temp_ad.set_trade_type("Pickup Off Campus")
            elif item_trade_option == '3':
                temp_ad.set_trade_type("Deliver to Home")
            ad_creation = "Ad title : " + temp_ad.get_ad_title() + '\n' + "Ad description: " + \
                          temp_ad.get_ad_description() + '\n' + "Ad price:"+temp_ad.get_ad_price() +\
                          '\n' + "Item category:"+temp_ad.get_item_category() + '\n' + "Item sub-category:" \
                          + temp_ad.get_item_sub_category() + '\n' + "Item condition:"+temp_ad.get_item_condition() \
                          + '\n'+"Trade Option:" + temp_ad.get_trade_type() + '\n' + "Date/Time:" + \
                          temp_ad.get_ad_date_time()
            user_consent = input("Do you want to post the following ad ? \nEnter 1 for Yes \nEnter 2 "
                                 "for No\n" + ad_creation+'\n')
            ad_template = temp_ad.get_ad_title() + ';' + temp_ad.get_ad_description() + ';' + \
                          temp_ad.get_ad_price() + ';' + temp_ad.get_item_category() + ';' + \
                          temp_ad.get_item_sub_category() + ';' + temp_ad.get_trade_type() + ';'\
                          + temp_ad.get_item_condition()+ ';' + temp_ad.get_ad_date_time()

            if user_consent == '1':
                with open("Advertisement.txt", 'a', encoding='utf-8') as infile:
                    infile.write(ad_template+'\n')
            elif user_consent == '2':
                self.post_ad()

        else:
            print("This feature is not available at the moment.")
            boundary = Boundary()
            boundary.display_main_menu()

    def ad_details(self, temp_ad):
        """
        accepts input value for creating ad

        :param temp_ad:
        :return:
        """

        temp_ad.set_ad_title(input("Enter ad title:\n"))
        temp_ad.set_ad_description(input("Enter ad description:\n"))
        temp_ad.set_ad_price(input("Enter ad price:\n"))
        now = datetime.datetime.now()
        temp_ad.set_ad_date_time(now.strftime("%Y-%m-%d %H:%M:%S"))

    def browse_ad(self):
        """

        helps user to browse the ad.

        :return:
        """
        with open('Advertisement.txt', 'r', encoding='utf8') as ads_data_file:
            for line in ads_data_file:
                tokens = line.split(';')
                ad_template_string = "Ad title : " + tokens[0] + '\n' + "Ad description: " + tokens[1]\
                                     + '\n' + "Ad price:" + tokens[2] + '\n' + "Item category:" + tokens[3] \
                                     + '\n' + "Item sub-category:" + tokens[4] + '\n' + "Item trade option:" \
                                     + tokens[5] + '\n' + "Item condition:" + tokens[6] + '\n' + "Date/Time:" \
                                     + tokens[7]
                print(ad_template_string)
                with open('Recentlyviewedads.txt', 'a', encoding='utf8') as recently_viewed_data:
                    recently_viewed_data.write(line)

    def recently_viewed_ads(self):
        """

        helps user to see the ads they have recently viewed

        :return:
        """
        with open('Recentlyviewedads.txt', 'r+', encoding='utf8') as recently_viewed_ads:
            for line in recently_viewed_ads:
                tokens = line.split(';')
                now = datetime.datetime.now()
                days = datetime.timedelta(3)
                today = now - days
                variable = tokens[-1].strip()
                ad_date_time = datetime.datetime.strptime(variable, "%Y-%m-%d %H:%M:%S")
                if ad_date_time > today:
                    recently_viewed_ad_template_string = "Ad title : " + tokens[0] + '\n' + "Ad description: "\
                                                         + tokens[1] + '\n' + "Ad price:" + tokens[2] + '\n' \
                                                         + "Item category:" + tokens[3] + '\n' + "Item sub-category:" +\
                                                         tokens[4] + '\n' + "Item trade type:" + tokens[5] + '\n'\
                                                         + "Item condition:" + tokens[6] + '\n' + "Date/time:" +\
                                                         tokens[7]
                    print(recently_viewed_ad_template_string)

    def previously_posted_ads(self):
        """

        shows the ads previously posted. not in current use.

        :return:
        """
        print("This feature is not available at the moment")
        boundary = Boundary()
        boundary.display_main_menu()

    def watchlist(self):
        """

        shows ads added to the watchlist by the user. Not in current use.

        :return:
        """
        print("This feature is not available at the moment")
        boundary = Boundary()
        boundary.display_main_menu()

    def log_out(self):
        """

        helps the user to exit the system.

        :return:
        """
        print("You have successfully exited the M.C.E.S System!\nPlease come again!")
        exit()


control = Control()
control.main()
