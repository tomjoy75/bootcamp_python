# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tjoyeux <tjoyeux@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 11:25:32 by tjoyeux           #+#    #+#              #
#    Updated: 2024/06/12 16:54:18 by tjoyeux          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pytest
from recipe import Recipe
from book import Book
from datetime import datetime

def test_valid_recipe():
    recipe = Recipe(
        "pizza", 
        3, 
        10, 
        ['tomates', 'pate', 'fromage'], 
        '', 
        'lunch'
    )
    assert recipe.name == "pizza"
    assert recipe.cooking_lvl == 3
    assert recipe.cooking_time == 10
    assert recipe.ingredients == ['tomates', 'pate', 'fromage']
    assert recipe.description == ''
    assert recipe.recipe_type == 'lunch'

def test_valid_book():
	my_book = Book("Italian food")
	assert my_book.name == "Italian food"
    
def test_recipe_empty_name():
    with pytest.raises(ValueError, match="name shouldn´t be empty"):
        Recipe("", 3, 10, ['tomates', 'pate', 'fromage'], '', 'lunch')

def test_recipe_invalid_name():
    with pytest.raises(ValueError, match="name should be String"):
        Recipe(5, 3, 10, ['tomates', 'pate', 'fromage'], '', 'lunch')

def test_book_empty_name():
	with pytest.raises(ValueError, match= "name shouldn´t be empty"):
		Book("")

def test_book_invalid_name():
	with pytest.raises(ValueError, match= "name should be String"):
		Book(5)
		
def test_invalid_cooking_lvl():
    with pytest.raises(ValueError, match="cooking_lvl between 1 and 5"):
        Recipe("pizza", 0, 10, ['tomates', 'pate', 'fromage'], '', 'lunch')

def test_invalid_cooking_time():
    with pytest.raises(ValueError, match="cooking_time should be an int"):
        Recipe("pizza", 3, "ten", ['tomates', 'pate', 'fromage'], '', 'lunch')

def test_empty_ingredients():
    with pytest.raises(ValueError, match="ingredients shouldn't be empty"):
        Recipe("pizza", 3, 10, [], '', 'lunch')

def test_invalid_ingredients():
    with pytest.raises(ValueError, match="each ingredient in list should be a string"):
        Recipe("pizza", 3, 10, ['tomates', 123, 'fromage'], '', 'lunch')

def test_invalid_recipe_type():
    with pytest.raises(ValueError, match="recipe_type should be starter/lunch/dessert"):
        Recipe("pizza", 3, 10, ['tomates', 'pate', 'fromage'], '', 'dinner')


if __name__ == "__main__":
    pizza = Recipe("pizza", 3, 10, ['tomates', 'pate', 'fromage'], '', 'lunch')
    pasta = Recipe("pasta", 5, 20, ['pates', 'sauce'], 'servir al dente', 'lunch')
    tiramisu = Recipe("tiramisu", 1, 30, ['cafe', 'creme fraiche', 'sucre'], 'accompagner d\'un bon cafe', 'dessert')
    
    print("---Recettes---\n")
    print(pizza)
    print(pasta)
    print(tiramisu)
    
    book = Book('Italian')
    book.add_recipe(pizza)
    book.add_recipe(pasta)
    book.add_recipe(tiramisu)
    
    print("---Livre de recettes---\n")
    print(book)
    
    print("---Test des methodes---\n")
    pytest.main(["-v", "test.py"])
#to_print = str(myRecipe)
