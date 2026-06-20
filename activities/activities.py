from fastapi import APIRouter

router = APIRouter()

@router.get('/activities')
def main():
    return 'This is the activities page'