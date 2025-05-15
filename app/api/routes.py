from fastapi import APIRouter, Depends
from app.services.chatbot_service import ChatbotService
from app.models.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.get('/ping')
async def ping_pong():
    """A simple ping endpoint."""
    return {"message": "pong!"}

@router.post('/chat', response_model=ChatResponse)
async def chat(request: ChatRequest, chatbot_service: ChatbotService = Depends(ChatbotService)):
    """Endpoint for chatbot interactions."""
    response = await chatbot_service.generate_response(request.message)
    return ChatResponse(response=response)