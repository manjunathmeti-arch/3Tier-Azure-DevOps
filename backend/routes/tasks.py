from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.task import Task
from db import get_database
from bson.objectid import ObjectId
import logging

router = APIRouter()

@router.post("/", response_model=Task)
async def create_task(task: Task, db=Depends(get_database)):
    try:
        task_dict = task.dict()
        result = await db.tasks.insert_one(task_dict)
        created_task = await db.tasks.find_one({"_id": result.inserted_id})
        return created_task
    except Exception as e:
        logging.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[Task])
async def get_tasks(db=Depends(get_database)):
    try:
        tasks = await db.tasks.find().to_list(1000)
        return tasks
    except Exception as e:
        logging.error(f"Error fetching tasks: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: str, task: Task, db=Depends(get_database)):
    try:
        updated_task = await db.tasks.find_one_and_update(
            {"_id": ObjectId(task_id)},
            {"$set": task.dict()},
            return_document=True
        )
        if updated_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return updated_task
    except Exception as e:
        logging.error(f"Error updating task: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{task_id}", response_model=dict)
async def delete_task(task_id: str, db=Depends(get_database)):
    try:
        delete_result = await db.tasks.delete_one({"_id": ObjectId(task_id)})
        if delete_result.deleted_count == 1:
            return {"message": "Task deleted"}
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        logging.error(f"Error deleting task: {e}")
        raise HTTPException(status_code=500, detail=str(e))
