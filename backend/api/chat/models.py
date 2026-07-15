from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
import uuid


class ChatMessage(SQLModel, table=True):
    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    
    message: str
    
    created_at: datetime = Field(
    default_factory=lambda: datetime.now(timezone.utc), 
    index=True,
    nullable=False
    )
    
class ChatMessagePayload(SQLModel):
    message: str


class ChatMessageListItem(ChatMessagePayload):
    created_at: datetime
    
    
class User(SQLModel, table=True):
    
    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    email: str = Field(unique=True, index=True)
    username: str
