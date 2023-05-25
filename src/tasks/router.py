from fastapi import APIRouter, Depends

from auth.base_config import current_user
from tasks.tasks import send_email_weekly_report

router = APIRouter(
    prefix='/report',
    tags=['CeleryTasks']
)


@router.get('/weekly_report')
def get_weekly_report(user=Depends(current_user)):
    send_email_weekly_report.delay(username=user.username)
    return {
        'status': 'success',
        'data': 'Email has been sent',
        'details': None
    }
