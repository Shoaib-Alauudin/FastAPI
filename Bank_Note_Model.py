from pydantic import BaseModel


class BankNote(BaseModel):
    # Define all parameter required as a inputs for Bank note classification
    variance: float
    skewness: float
    curtosis: float
    entropy: float