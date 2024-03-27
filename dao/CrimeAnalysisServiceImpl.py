import pyodbc
from typing import Collection, List
from dao.ICrimeAnalysisService import ICrimeAnalysisService
from util.PropertyUtil import PropertyUtil
from util.DBConnection import DBConnection
from entity.Incident import Incident
from entity.Case import Case

class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    connection = None

    def __init__(self):
        self.connection = DBConnection.get_connection()

    def create_incident(self, incident) -> bool:
        try:
            if self.connection is None:
                print("Database connection is not initialized.")
                return False
            
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Incidents (IncidentType, IncidentDate, Location, Description, Status, VictimID, SuspectID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (incident.incident_type, incident.incident_date, incident.location, incident.description, incident.status, incident.victim_id, incident.suspect_id))
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error occurred while creating incident: {e}")
            return False

    def update_incident_status(self, status, incident_id) -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Incidents SET Status = ? WHERE IncidentID = ?", (status, incident_id))
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error occurred while updating incident status: {e}")
            return False

    def get_incidents_in_date_range(self, start_date, end_date) -> Collection:
        incidents = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Incidents WHERE IncidentDate BETWEEN ? AND ?", (start_date, end_date))
            rows = cursor.fetchall()
            for row in rows:
                incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                incidents.append(incident)
        except pyodbc.Error as e:
            print(f"Error occurred while retrieving incidents in date range: {e}")
        return incidents

    def search_incidents(self, criteria) -> Collection:
        incidents = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Incidents WHERE IncidentType = ?", (criteria,))
            rows = cursor.fetchall()
            for row in rows:
                incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                incidents.append(incident)
        except pyodbc.Error as e:
            print(f"Error occurred while searching incidents: {e}")
        return incidents

    def generate_incident_report(self, incident) -> bool:
        try:
            # Placeholder implementation
            print("Generating incident report...")
            return True
        except pyodbc.Error as e:
            print(f"Error occurred while generating incident report: {e}")
            return False

    def create_case(self, case_description: str, incidents: Collection[Incident]) -> 'Case':
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Cases (CaseDescription) VALUES (?)", (case_description,))
            self.connection.commit()
            case_id = cursor.lastrowid
            for incident in incidents:
                cursor.execute("INSERT INTO CaseIncidents (CaseID, IncidentID) VALUES (?, ?)", (case_id, incident.incident_id))
            self.connection.commit()
            return Case(case_id, case_description, incidents)
        except pyodbc.Error as e:
            print(f"Error occurred while creating case: {e}")
            return None

    def get_case_details(self, case_id: int) -> 'Case':
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Cases WHERE CaseID = ?", (case_id,))
            row = cursor.fetchone()
            if row:
                case_description = row[1]
                cursor.execute("SELECT IncidentID FROM CaseIncidents WHERE CaseID = ?", (case_id,))
                incident_ids = [incident[0] for incident in cursor.fetchall()]
                incidents = self._get_incidents_by_ids(incident_ids)
                return Case(case_id, case_description, incidents)
            else:
                print(f"No case found with ID: {case_id}")
                return None
        except pyodbc.Error as e:
            print(f"Error occurred while retrieving case details: {e}")
            return None

    def update_case_details(self, case_obj: 'Case') -> bool:
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Cases SET CaseDescription = ? WHERE CaseID = ?", (case_obj.case_description, case_obj.case_id))
            self.connection.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error occurred while updating case details: {e}")
            return False

    def get_all_cases(self) -> List['Case']:
        cases = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Cases")
            rows = cursor.fetchall()
            for row in rows:
                case_id = row[0]
                case_description = row[1]
                cursor.execute("SELECT IncidentID FROM CaseIncidents WHERE CaseID = ?", (case_id,))
                incident_ids = [incident[0] for incident in cursor.fetchall()]
                incidents = self._get_incidents_by_ids(incident_ids)
                case = Case(case_id, case_description, incidents)
                cases.append(case)
        except pyodbc.Error as e:
            print(f"Error occurred while retrieving all cases: {e}")
        return cases

    def _get_incidents_by_ids(self, incident_ids: List[int]) -> List['Incident']:
        incidents = []
        try:
            cursor = self.connection.cursor()
            for incident_id in incident_ids:
                cursor.execute("SELECT * FROM Incidents WHERE IncidentID = ?", (incident_id,))
                row = cursor.fetchone()
                if row:
                    incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    incidents.append(incident)
            return incidents
        except pyodbc.Error as e:
            print(f"Error occurred while retrieving incidents by IDs: {e}")
            return []
