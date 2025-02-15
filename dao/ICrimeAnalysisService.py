from abc import ABC, abstractmethod
from typing import Collection, List
from entity.Incident import Incident
from entity.Report import Report
from entity.Case import Case
from entity.Status import Status

class ICrimeAnalysisService(ABC):
    @abstractmethod
    def create_incident(self, incident) -> bool:
        pass

    @abstractmethod
    def update_incident_status(self, status, incident_id) -> bool:
        pass

    @abstractmethod
    def get_incidents_in_date_range(self, start_date, end_date) -> Collection:
        pass

    @abstractmethod
    def search_incidents(self, criteria) -> Collection:
        pass

    @abstractmethod
    def generate_incident_report(self, incident):
        pass

    @abstractmethod
    def create_case(self, case_description: str, incidents: Collection) -> 'Case':
        pass

    @abstractmethod
    def get_case_details(self, case_id: int) -> 'Case':
        pass

    @abstractmethod
    def update_case_details(self, case_obj: 'Case') -> bool:
        pass

    @abstractmethod
    def get_all_cases(self) -> List['Case']:
        pass
