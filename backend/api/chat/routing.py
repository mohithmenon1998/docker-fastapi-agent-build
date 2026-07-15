from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session, select, col
from api.chat.models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session
import uuid
router = APIRouter()

@router.get("/health")
def chat_health():
    return {"system":"ok"}

@router.post("/messages/create", response_model= ChatMessageListItem)
def create_chat_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):    
    data = payload.model_dump()
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
    
@router.get("/messages/recent", response_model= List[ChatMessageListItem])
def list_chat_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage).order_by(col(ChatMessage.created_at).desc()).limit(10)
    results = session.exec(query).all()
    return results

@router.get("/messages/{message_id}", response_model= ChatMessageListItem)
def get_chat_message(message_id: uuid.UUID, session: Session = Depends(get_session)):
    db_message = session.get(ChatMessage, message_id)
    if not db_message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Message with ID {message_id} not found"
        )
    return db_message

@router.delete("/messages/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_chat_message(message_id: uuid.UUID, session: Session = Depends(get_session)):
    db_message = session.get(ChatMessage, message_id)
    if not db_message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Message with ID {message_id} not found"
        )
        
    session.delete(db_message)
    session.commit()
    return None