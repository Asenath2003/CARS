class Victim:
    def __init__(self, victimID=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactInfo=None):
        self._victimID = victimID
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._gender = gender
        self._contactInfo = contactInfo

    def get_victimID(self):
        return self._victimID

    def set_victimID(self, victimID):
        self._victimID = victimID

    def get_firstName(self):
        return self._firstName

    def set_firstName(self, firstName):
        self._firstName = firstName

    def get_lastName(self):
        return self._lastName

    def set_lastName(self, lastName):
        self._lastName = lastName

    def get_dateOfBirth(self):
        return self._dateOfBirth

    def set_dateOfBirth(self, dateOfBirth):
        self._dateOfBirth = dateOfBirth

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_contactInfo(self):
        return self._contactInfo

    def set_contactInfo(self, contactInfo):
        self._contactInfo = contactInfo