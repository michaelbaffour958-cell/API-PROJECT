from fastapi import APIRouter

router = APIRouter()

@router.get('/register')
def registering():
    return {
        'message': 'You are on the registration page'
    }
if __name__ == '__main__':
    registering()