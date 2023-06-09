from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy import relationship

from database import Base


class Disease(Base):
    __tablename__ = "disease"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    slug = Column(String)
    type = Column(String)
    excerpt = Column(String)
    body = Column(String)
    image = Column(String)


class Advice(Base):
    __tablename__ = "advice"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    advice = Column(String)
    created_at = Column(String)
