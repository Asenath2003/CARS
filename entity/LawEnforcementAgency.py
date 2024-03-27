class LawEnforcementAgency:
    def __init__(self, agencyID=None, agencyName=None, jurisdiction=None, contactInfo=None):
        self._agencyID = agencyID
        self._agencyName = agencyName
        self._jurisdiction = jurisdiction
        self._contactInfo = contactInfo

    def get_agencyID(self):
        return self._agencyID

    def set_agencyID(self, agencyID):
        self._agencyID = agencyID

    def get_agencyName(self):
        return self._agencyName

    def set_agencyName(self, agencyName):
        self._agencyName = agencyName

    def get_jurisdiction(self):
        return self._jurisdiction

    def set_jurisdiction(self, jurisdiction):
        self._jurisdiction = jurisdiction

    def get_contactInfo(self):
        return self._contactInfo

    def set_contactInfo(self, contactInfo):
        self._contactInfo = contactInfo