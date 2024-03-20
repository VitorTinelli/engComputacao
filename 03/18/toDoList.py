## To Do List 
## Author: Vitor Muneretto Tinelli
## Date: 18/03/2024
## Description: This program is a to do list that allows the user to add, remove, and list tasks. (Using lists)
## Engenharia da Computação UNISATC | Estrutura de Dados | Prof. Christiane Vieira 

import time
import os


toDoList = []

## Função para adicionar uma tarefa
def addTask():
  op = input("Write A to add a task in the last position or B to add in a specific position (X to cancel): ")
  print("")
  ## Add a task na última posição
  if op.upper() == "A":
    task = input("Write the task: ")
    toDoList.append(task)
    print("Task added successfully")

  ## Add a task em uma posição específica
  elif op.upper() == "B":
    task = input("Write the task: ")
    position = int(input("Write the position: "))

    ## Check if the position is valid
    if position == 0 or position <= len(toDoList): # Se a posição for 0 ou menor que o tamanho da lista
      toDoList.insert(position, task) # Adiciona a tarefa na posição
      print("Task added successfully")
    else:
      print("Invalid position, try again!") 
      print("List Length: ", len(toDoList))

  ## Cancelar a operação (Adicionar task)
  elif op.upper() == "X":
    print("Operation canceled")

  ## Opção inválida, chama a função novamente
  else:
    print("Invalid option, try again")
    addTask()



## Função para remover uma tarefa, mesma logica do adicionar
def removeTask():
  print("")
  if len(toDoList) == 0:
    print("The list is empty")
    return
  
  op = input("Write A to remove by task name or B to remove by task position (X to cancel): ")
  if op.upper() == "A":
    task = input("Write the task: ")
    try: # Tenta remover a tarefa (caso exista na lista)
      toDoList.remove(task)
      print("Task removed successfully")
    except: # Caso não exista
      print("Task not found")

  elif op.upper() == "B":
    position = int(input("Write the position: "))
    if position >= 0 and position < len(toDoList):
      toDoList.pop(position)
      print("Task removed successfully")
    else:
      print("Invalid position, try again")
      print("List Length: ", len(toDoList))

  elif op.upper() == "X":
    print("Operation canceled")

  else:
    print("Invalid option, try again")
    removeTask()

## Função para listar as tarefas
def listTasks():
  op = input("Write A to list by name or B to list by position or C to list all(X to cancel): ")
  print("")

  if op.upper() == "A":
    value = input("Write the task: ")
    try:
      print(toDoList.index(value), " - ", value)
    except:
      print("Task not found")

  elif op.upper() == "B":
    position = int(input("Write the position: "))
    if position >= 0 and position < len(toDoList):
      print(toDoList[position])
    else:
      print("Invalid position, try again")
      print("List Length: ", len(toDoList))
  elif op.upper() == "C":
    for i in range(len(toDoList)):
      print(i, " - ", toDoList[i])

  elif op.upper() == "X":
    print("Operation canceled")
  else:
    print("Invalid option, try again")
    listTasks()

## Menu principal
def main():
  while (True):
    print("\n\n\n")
    print("To Do List")
    print("1 - Add a task")
    print("2 - Remove a task")
    print("3 - List tasks")
    print("4 - Exit")
    op = int(input("Choose an option: "))


    ## Verifica a opção escolhida
    try:
      if op == 1:
        time.sleep(0.4)
        print("\n\n\n\n\n\n\n\n")
        addTask() # executa a função para adicionar tarefas

      elif op == 2:
        time.sleep(0.4)
        print("\n\n\n\n\n\n\n\n")
        removeTask() # executa a função para remover tarefas

      elif op == 3:
        time.sleep(0.4)
        print("\n\n\n\n\n\n\n\n")
        listTasks() # executa a função para listar tarefas

      elif op == 4:
        print("\n\n\n\n\n\n\n\n")
        print("Exiting in 3")
        time.sleep(1)
        print("Exiting in 2")
        time.sleep(1)
        print("Exiting in 1")
        time.sleep(1)
        print("Exited")
        break

    ## Caso a opção seja inválida 
    except:
      print("Invalid option, try again")


if __name__ == "__main__":
  main()
    
  


