from pydantic import BaseModel


class FormattedMsg(BaseModel):
    text: str
    img_path: str
