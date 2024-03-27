class Evidence:
    def __init__(self, evidenceID=None, description=None, locationFound=None, incidentID=None):
        self._evidenceID = evidenceID
        self._description = description
        self._locationFound = locationFound
        self._incidentID = incidentID

    def get_evidenceID(self):
        return self._evidenceID

    def set_evidenceID(self, evidenceID):
        self._evidenceID = evidenceID

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_locationFound(self):
        return self._locationFound

    def set_locationFound(self, locationFound):
        self._locationFound = locationFound

    def get_incidentID(self):
        return self._incidentID

    def set_incidentID(self, incidentID):
        self._incidentID = incidentID

