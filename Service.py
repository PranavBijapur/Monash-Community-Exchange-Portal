from Advertisement import Advertisement


class Service(Advertisement):

    def __init__(self, service_category, service_aoe, service_faculty):
        """

        :param service_category:
        :param service_aoe:
        :param service_faculty:
        """
        self.service_category = service_category
        self.service_aoe = service_aoe
        self.service_faculty = service_faculty

    def get_service_category(self):
        """

        :return:
        """
        return self.service_category

    def set_service_category(self, service_category):
        """

        :param service_category:
        :return: string
        """
        self.service_category = service_category

    def get_service_aoe(self):
        """

        :return:string
        """
        return self.service_aoe

    def set_service_aoe(self, service_aoe):
        """

        :param service_aoe:
        :return:string
        """
        self.service_aoe = service_aoe

    def get_service_faculty(self):
        """

        :return: string
        """
        return self.service_faculty

    def set_service_faculty(self, service_faculty):
        """

        :param service_faculty:
        :return: string
        """
        self.service_faculty = service_faculty

