import os
import time
from pprint import pprint

#HOMEWORK BELOW


def r_file(): #func of reading file
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_id = line.strip()#var of name txt reading
            count = int(f.readline())
            comp_list = list()#var of components list
            for item in range(count):
                comps = {}# var for components values
                comp_t = f.readline().strip()#var of txt reading
                comps['ingredient_name'], comps['quantity'], comps['measure'] = comp_t.split('|')
                comps['quantity'] = int(comps['quantity'])
                comp_list.append(comps)
            f.readline()
            cook_book[dish_id] = comp_list
    return cook_book




def get_shop_list_by_dishes(dishes, people):
    comp_dict = dict()#new dict of component list

    for dish_id in dishes:  # cycle of dishes
        if dish_id in cook_book:
            for ingridients in cook_book[dish_id]:  # cycle of components in dish
                calc_val_quantity = dict()
                if ingridients['ingredient_name'] not in comp_dict:
                    calc_val_quantity['measure'] = ingridients['measure']
                    calc_val_quantity['quantity'] = ingridients['quantity'] * people
                    comp_dict[ingridients['ingredient_name']] = calc_val_quantity
                else:
                    comp_dict[ingridients['ingredient_name']]['quantity'] = comp_dict[ingridients['ingredient_name']]['quantity'] + \
                                                                     ingridients['quantity'] * people

        else:
            print(f'\n"No dish in list, bro"\n')
    return comp_dict





def rw_file_function(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        os.chdir('sorted')
        output_file = "rw_file_function.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(output_file, 'w', encoding='utf-8') as full_output:

            if len(file1) < len(file2) and len(file1) < len(file3):
                full_output.write(path1 + '\n')
                full_output.write(str(len(file1)) + '\n')
                full_output.writelines(file1)
                full_output.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                full_output.write(path2 + '\n')
                full_output.write(str(len(file2)) + '\n')
                full_output.writelines(file2)
                full_output.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                full_output.write(path3 + '\n')
                full_output.write(str(len(file3)) + '\n')
                full_output.writelines(file3)
                full_output.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                full_output.write(path1 + '\n')
                full_output.write(str(len(file1)) + '\n')
                full_output.writelines(file1)
                full_output.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                full_output.write(path2 + '\n')
                full_output.write(str(len(file2)) + '\n')
                full_output.writelines(file2)
                full_output.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                full_output.write(path3 + '\n')
                full_output.write(str(len(file3)) + '\n')
                full_output.writelines(file3)
                full_output.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                full_output.write(path1 + '\n')
                full_output.write(str(len(file1)) + '\n')
                full_output.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                full_output.write(path2 + '\n')
                full_output.write(str(len(file2)) + '\n')
                full_output.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                full_output.write(path3 + '\n')
                full_output.write(str(len(file3)) + '\n')
                full_output.writelines(file3)
    else:
        print('Without params, bro')
    return


if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = r_file()
    print('Task 1*_*_*_*_*_*_*_*_*_*_*_*')
    time.sleep(1)#delay for output
    pprint(cook_book)
    print('Task 2*_*_*_*_*_*_*_*_*_*_*_*')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], people=1))

    time.sleep(2)
    print('Task 3*_*_*_*_*_*_*_*_*_*_*_*')
    rw_file_function()