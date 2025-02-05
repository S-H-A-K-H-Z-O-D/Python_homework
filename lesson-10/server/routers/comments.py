from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Comment
from schemas import Comment as CommentSchema, CommentCreate

router = APIRouter(prefix="/comments", tags=["comments"])

@router.get("/", response_model=List[CommentSchema])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Comment).offset(skip).limit(limit).all()

@router.post("/", response_model=CommentSchema)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    db_comment = Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.get("/{comment_id}", response_model=CommentSchema)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.put("/{comment_id}", response_model=CommentSchema)
def update_comment(comment_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    for key, value in comment.dict().items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.delete("/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(db_comment)
    db.commit()
    return {"message": "Comment deleted"}
