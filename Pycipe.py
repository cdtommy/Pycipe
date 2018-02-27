import sys
import os
from time import sleep

#Cole Duersch
#February 26 2018 18:02 MST
# This software is licensed under the GNU General Public License
# To read more about the GPL see the License.txt file included in the git or view it here www.gnu.org/licenses/gpl-3.0.txt
KnownRecipes = ['Scrambled Eggs', 'Bacon', 'Quesadilla']

def Ques():
	os.system('clear')
	print('Recipie Yields 1 serving')
	ingredients = '2 tortillas, premade or cooked \n 5 slices of cheese of your preference.'
	print('Ingredients')
	print('-----------')
	print(ingredients)
	print('\n')
	instructions = '1. Put 1 tortilla on a plate. \n 2. Cover tortilla with cheese slices. \n 3. Microwave on high for 30 seconds.'
	print(instructions)
	print('\n')
	print('Is there anything else you would like to make today?')
	ans = raw_input('> ')
	if ans == 'yes':
		UserRecipe()
	else:
		sys.exit()




def ScramEggs():
	os.system('clear')
	print('Recipe Yields 2 servings')
	ingredients = '4 Eggs \n 1/4 cup or 59 mL milk \n Salt and Pepper, to taste \n 2 tsp butter'
	print('Ingredients')
	print('-----------')
	print(ingredients)
	print('\n')
	instructions = '1. Beat eggs, milk, salt and pepper in medium bowl until blended \n 2. Heat butter in a large skillet over medium heat \n 3. Pour in egg mixture. As the eggs set, gently pull the eggs across the pan with a spatula, forming large soft curds \n 4. Continue cooking until thickened and no visible liquid egg remains'
	print(instructions)
	print('\n')
	print('Is there anything else you would like to make today?')
	ans = raw_input('> ')
	if ans == 'yes':
		UserRecipe()
	else:
		sys.exit()

def BaconFunc():
	os.system('clear')
	print('Recipe Yields 4 servings')
	ingredients = 'Four 4 strips of bacon\n Pinch Salt\n Pinch Pepper\n'
	print('Ingredients')
	print('-----------')
	print(ingredients)
	print('\n')
	instructions = '1. Put bacon in skillet with a pad of butter. \n 2. Sprinkle salt and pepper over bacon.'
	print(instructions) 
	print ('\n')
	print('Is there anything else you would like to make today?')
	ans = raw_input('> ')
	if ans == 'yes':
		UserRecipe()
	else:
		sys.exit()
		
def UserRecipe():
	os.system('clear')
	print('What would you like to make today?')
	recipe = raw_input('> ')
	print(recipe)
	if recipe == ('Scrambled Eggs'):
		ScramEggs()
	if recipe == ('Bacon') :
	 BaconFunc()
	if recipe == ('Quesadilla'):
		Ques()
	if recipe not in KnownRecipes:
		print('Sorry that recipe is not available')
		
UserRecipe()
	


