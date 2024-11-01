from Advertisement import Advertisement


class Item(Advertisement):
    """

    """
    def __init__(self, item_category=" ", item_sub_category=" ", item_condition=" "):
        """

        :param item_category:
        :param item_sub_category:
        :param item_condition:
        """
        self.item_category = item_category
        self.item_sub_category = item_sub_category
        self.item_condition = item_condition

    def get_item_category(self):
        """
        accessor method for  item_category
        :return: string
        """
        return self.item_category

    def set_item_category(self, item_category):
        """
        mutator method for item_category
        :param item_category:
        :return: string
        """
        self.item_category = item_category

    def get_item_sub_category(self):
        """
        accessor method for  item_sub_category
        :return: string
        """
        return self.item_sub_category

    def set_item_sub_category(self, item_sub_category):
        """
        mutator method for item_sub_category
        :param item_sub_category:
        :return: string
        """
        self.item_sub_category = item_sub_category

    def get_item_condition(self):
        """
        accessor method for  item_condition
        :return: string
        """
        return self.item_condition

    def set_item_condition(self, item_condition):
        """
        mutator method for item_condition
        :param item_condition:
        :return: string
        """
        self.item_condition = item_condition
