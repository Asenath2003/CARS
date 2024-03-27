class Suspect:
    def __init__(self, suspectID=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactInfo=None):
        self._suspectID = suspectID
        self._firstName = firstName
        self._lastName = lastName
        self._dateOfBirth = dateOfBirth
        self._gender = gender
        self._contactInfo = contactInfo

    def get_suspectID(self):
        return self._suspectID

    def set_suspectID(self, suspectID):
        self._suspectID = suspectID

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
