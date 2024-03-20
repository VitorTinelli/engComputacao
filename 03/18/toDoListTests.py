import unittest


## Testes Unitários para o To Do List
## Author: Vitor Muneretto Tinelli
## Date: 18/03/2024
## Description: This program contains the unit tests for the to do list program.
## Engenharia da Computação UNISATC | Estrutura de Dados | Prof. Christiane Vieira 

class TestToDoList(unittest.TestCase):
  def test_addByName_SuccessfulWhenInsertGoesFine(self):
    toDoList = []
    task = "Comprar Batata"
    toDoList.append(task)
    self.assertEqual(toDoList[0], task) # Teste Passou


  def test_addByID_SuccessfulWhenInsertGoesFine(self):
      toDoList = ["Buy Books", "Study", "Make a test"]
      task = "Buy Potato"
      position = 1
      if position == 0 or position <= len(toDoList): 
        toDoList.insert(position, task) 
        self.assertEqual(toDoList[position], task) # Teste Passou
      else:
        self.assertTrue(False) # Teste Falhou


  def test_addByID_SuccessfulWhenInsertGoesBad(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    task = "Buy Potato"
    position = 5
    if position == 0 or position <= len(toDoList): 
      toDoList.insert(position, task) 
      self.assertNotEqual(toDoList[position], task) # Teste Falhou
    else:
      self.assertTrue(True) # Teste Passou

  def test_removeByName_SuccessfulWhenRemoveGoesFine(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    task = "Buy Books"
    try:
      toDoList.remove(task)
    except:
      self.assertTrue(False) # Teste Falhou
    self.assertNotIn(task, toDoList) # Teste Passou

  def test_removeByName_SuccessfulWhenRemoveGoesBad(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    task = "Buy Potato"
    try:
      toDoList.remove(task)
    except:
      self.assertTrue(True) # Teste Passou
    self.assertNotIn(task, toDoList) # Teste Falhou

  def test_removeByID_SuccessfulWhenRemoveGoesFine(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    position = 1
    if position >= 0 and position < len(toDoList):
      toDoList.pop(position)
    else:
      self.assertTrue(False) # Teste Falhou
    self.assertNotIn("Study", toDoList) # Teste Passou

  def test_removeByID_SuccessfulWhenRemoveGoesBad(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    position = 5
    if position >= 0 and position < len(toDoList):
      toDoList.pop(position)
      self.assertTrue(False) # Teste Falhou
    else:
      self.assertTrue(True) # Teste Passou
    self.assertIn("Make a test", toDoList) # Teste Passou

  def test_listTasksBy_SuccessfulWhenListGoesFine(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    self.assertEqual(len(toDoList), 3) # Teste Passou

  def test_listTasksByPosition_SuccessfulWhenListGoesFine(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    position = 1
    if position >= 0 and position < len(toDoList):
      self.assertEqual(toDoList[position], "Study") # Teste Passou
    else:
      self.assertTrue(False) # Teste Falhou
  def test_listTasksByPosition_SuccessfulWhenListGoesBad(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    position = 5
    if position >= 0 and position < len(toDoList):
      self.assertEqual(toDoList[position], "falhou teste") # Teste Falhou
    else:
      self.assertTrue(True) # Teste Passou 

  def test_listTasksByName_SuccessfulWhenListGoesFine(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    task = "Study"
    try:
      self.assertEqual(toDoList.index(task), 1) # Teste Passou
    except:
      self.assertTrue(False) # Teste Falhou
  
  def test_listTasksByName_SuccessfulWhenListGoesBad(self):
    toDoList = ["Buy Books", "Study", "Make a test"]
    task = "Study"
    try:
      self.assertEqual(toDoList.index(task), 5) # Teste Falhou
    except:
      self.assertTrue(True) # Teste Passou

if __name__ == '__main__':
  unittest.main()