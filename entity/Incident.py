class Incident:
    def __init__(self, incident_id=None, description=None, date=None, incident_type=None,
                 latitude=None, longitude=None, status=None, victim_id=None, suspect_id=None, agency_id=None):
        self._incident_id = incident_id
        self._description = description
        self._date = date
        self._incident_type = incident_type
        self._latitude = latitude
        self._longitude = longitude
        self._status = status
        self._victim_id = victim_id
        self._suspect_id = suspect_id
        self._agency_id = agency_id

    def get_incident_id(self):
        return self._incident_id

    def set_incident_id(self, incident_id):
        self._incident_id = incident_id

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_incident_type(self):
        return self._incident_type

    def set_incident_type(self, incident_type):
        self._incident_type = incident_type

    def get_latitude(self):
        return self._latitude

    def set_latitude(self, latitude):
        self._latitude = latitude

    def get_longitude(self):
        return self._longitude

    def set_longitude(self, longitude):
        self._longitude = longitude

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_victim_id(self):
        return self._victim_id

    def set_victim_id(self, victim_id):
        self._victim_id = victim_id

    def get_suspect_id(self):
        return self._suspect_id

    def set_suspect_id(self, suspect_id):
        self._suspect_id = suspect_id

    def get_agency_id(self):
        return self._agency_id

    def set_agency_id(self, agency_id):
        self._agency_id = agency_id
