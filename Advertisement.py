import datetime


class Advertisement:

    """
    Attributes:
        ad_title: title of the ad
        ad_description: description of the ad
        ad_trade_type: ad trade option
        ad_price: price of the commodity in the ad
        ad_date_time:date/time at which the ad was posted.
    Methods:
        get_ad_title():
        accessor method for ad_title.

        set_ad_title():
        mutator method for ad_title.

        get_ad_description():
        accessor method for ad_description

        set_ad_description():
        mutator method for ad_description

        get_trade_type():
        accessor method for  ad_trade_type.


        set_trade_type():
        mutator method for ad_trade_type


        set_ad_price():
        mutator method for ad_price

        get_ad_price():
        accessor method for ad_price

        get_ad_date_time():
        accessor method for ad_date_time


        set_ad_date_time():
        mutator method for ad_date_time

    """

    def __init__(self, ad_title="", ad_description="", ad_trade_type="", ad_price=-1, ad_date_time=""):
        """

        :param ad_title:
        :param ad_description:
        :param ad_trade_type:
        :param ad_price:
        :param ad_date_time:
        """
        self.ad_title = ad_title
        self.ad_description = ad_description
        self.ad_trade_type = ad_trade_type
        self.ad_price = ad_price
        self.ad_date_time = ad_date_time


    def get_ad_title(self):
        """

        :return:
        """
        return self.ad_title

    def set_ad_title(self, ad_title):
        """

        :param ad_title:
        :return:
        """
        self.ad_title = ad_title

    def get_ad_description(self):
        """

        :return:
        """
        return self.ad_description

    def set_ad_description(self, ad_description):
        """

        :param ad_description:
        :return:
        """
        self.ad_description = ad_description

    def get_trade_type(self):
        """

        :return:
        """
        return self.ad_trade_type

    def set_trade_type(self, ad_trade_type):
        """

        :param ad_trade_type:
        :return:
        """
        self.ad_trade_type = ad_trade_type

    def get_ad_price(self):
        """

        :return:
        """
        return self.ad_price

    def set_ad_price(self, ad_price):
        """

        :param ad_price:
        :return:
        """
        self.ad_price = ad_price

    def get_ad_date_time(self):
        """

        :return:
        """
        return self.ad_date_time

    def set_ad_date_time(self, ad_date_time):
        """

        :param ad_date_time:
        :return:
        """
        self.ad_date_time = ad_date_time
