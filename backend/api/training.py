from fastapi import APIRouter
from services.automl_service import AutoMLService

router = APIRouter()

@router.post("/train")
async def train_model(
    file_path: str,
    target: str
):

    service = AutoMLService()

    result = service.train(
        file_path,
        target
    )

    return {
        "accuracy": result["score"]
    }
