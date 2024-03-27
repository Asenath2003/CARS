class Officer:
    def __init__(self, officerID=None, firstName=None, lastName=None, badgeNumber=None, rank=None, contactInfo=None, agencyID=None):
        self._officerID = officerID
        self._firstName = firstName
        self._lastName = lastName
        self._badgeNumber = badgeNumber
        self._rank = rank
        self._contactInfo = contactInfo
        self._agencyID = agencyID

    def get_officerID(self):
        return self._officerID

    def set_officerID(self, officerID):
        self._officerID = officerID

    def get_firstName(self):
        return self._firstName

    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_lastName(self):
        return self._lastName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_badgeNumber(self):
        return self._badgeNumber

    def set_badgeNumber(self, badgeNumber):
        self._badgeNumber = badgeNumber

    def get_rank(self):
        return self._rank

    def set_rank(self, rank):
        self._rank = rank

    def get_contactInfo(self):
        return self._contactInfo

    def set_contactInfo(self, contactInfo):
        self._contactInfo = contactInfo

    def get_agencyID(self):
        return self._agencyID

    def set_agencyID(self, agencyID):
        self._agencyID = agencyID