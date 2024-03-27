class Report:
    def __init__(self, reportID=None, incidentID=None, reportingOfficerID=None, reportDate=None, reportDetails=None, status=None):
        self._reportID = reportID
        self._incidentID = incidentID
        self._reportingOfficerID = reportingOfficerID
        self._reportDate = reportDate
        self._reportDetails = reportDetails
        self._status = status

    def get_reportID(self):
        return self._reportID

    def set_reportID(self, reportID):
        self._reportID = reportID

    def get_incidentID(self):
        return self._incidentID

    def set_incidentID(self, incidentID):
        self._incidentID = incidentID

    def get_reportingOfficerID(self):
        return self._reportingOfficerID

    def set_reportingOfficerID(self, reportingOfficerID):
        self._reportingOfficerID = reportingOfficerID

    def get_reportDate(self):
        return self._reportDate

    def set_reportDate(self, reportDate):
        self._reportDate = reportDate

    def get_reportDetails(self):
        return self._reportDetails

    def set_reportDetails(self, reportDetails):
        self._reportDetails = reportDetails

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status