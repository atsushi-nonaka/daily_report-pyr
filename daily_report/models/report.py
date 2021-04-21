from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    text,
    Text
)

from sqlalchemy.dialects.mysql import (
    BIGINT,
    TIMESTAMP,
    TINYINT
)

from .meta import Base, CustomMixIn

class Report(Base, CustomMixIn):
    __tablename__ = 'reports'
    
    id = Column(BIGINT(20), primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    report_date = Column(Date, nullable=False)
    user_id = Column(BIGINT(20), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

