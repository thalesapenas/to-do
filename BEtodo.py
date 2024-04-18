from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4
from fastapi.middleware import Middleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=[''],
        allow_credentials=True,
        allow_methods=[''],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)



class task(BaseModel):
    id: Optional[str]= None
    nome: str
    is_done: bool = False

banco: List[task] = []

@app.get("/") # listar tarefas
def bem_vindo():
    return "fala, izaias! bem vindo ao Back end do to-do!"

@app.get("/task") # listar tarefas
def lista_de_tarefas():
    return banco

@app.get("/task/{task_id}")# buscar tarefa especifica
def find_task(task_id: str):
    for task in banco:
        if task.id == task_id:
            return task
    return "A tarefa não existe!"

@app.delete("/task/{task_id},")#excluir tarefa
def remove_task(task_id: str):
    for task in banco:
        if task.id == task_id:
            banco.remove(task)
            return "tarefa removida!"
    return "A tarefa não existe!"

@app.post("/task")#criar tarefa
def create_task(task1: task):
    for task in banco:
        if task.nome == task1.nome:
            return "A tarefa já existe!"
    task1.id = str(uuid4())
    banco.append(task1)
    return "tarefa criada com sucesso"

@app.put("/task_update_name/{task_id}")#atualizar tarefa nome da tarefa
def update(task_id:str, task_nome:str):
    for task in banco:
        if task.id == task_id:
            break
        return "A tarefa não existe!"
    task.nome = task_nome
    return "Tarefa atualizada com sucesso!"


@app.put("/task_update_True/{task_id}")#atualizar status da tarefa pra false
def update(task_id:str):
    for task in banco:
        if task.id == task_id:
            break
        return "A tarefa não existe!"
    task.is_done = True
    return "Tarefa atualizada com sucesso!"

@app.put("/task_update_False/{task_id}")#atualizar status da tarefa pra true
def update(task_id:str):
    for task in banco:
        if task.id == task_id:
            break
        return "A tarefa não existe!"
    task.is_done = False
    return "Tarefa atualizada com sucesso!"




