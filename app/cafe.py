import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("You dont`t have the vaccine")
        if visitor["vaccine"].get("expiration_date") < datetime.date.today():
            raise OutdatedVaccineError("You have the outdated vaccine")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("You are not wearing a MASK!!!")
        return f"Welcome to {self.name}"