# 데이터베이스/템플릿 관련 설정
from fastapi.templating import Jinja2Templates

BoradDB_NAME = "board.db"
MemberDB_NAME = "member.db"

templates = Jinja2Templates(directory="templates")