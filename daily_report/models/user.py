from sqlalchemy import (
    Column,
    Integer,
    String,
    text
)

from sqlalchemy.dialects.mysql import (
    BIGINT,
    TIMESTAMP,
    TINYINT
)

from .meta import Base, CustomMixIn

class User(Base, CustomMixIn):
    __tablename__ = 'users'
    
    id = Column(BIGINT(20), primary_key=True)
    name = Column(String(255), nullable=False)
    mail_address = Column(String(255) , nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    deleted = Column(TINYINT, nullable=False, default=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

