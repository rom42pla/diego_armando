from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class User(BaseModel):
    date_subscribtion: datetime
    date_expiration: datetime
    id: UUID = Field(default_factory=uuid4)
    id_telegram: str
    name: str