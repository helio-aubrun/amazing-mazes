import random

directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
list_cells = []
groups = []

char_wall = "#"
char_empty = "."

labyrinthe = []


def init_labyrinthe(n):
    labyrinthe = [["#"] * (n) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i % 2 != 0 and j % 2 != 0:
                labyrinthe[i][j] = char_empty

    return labyrinthe


def init_list_cells(labyrinthe, n):
    for line in range(n):
        for column in range(n):
            if labyrinthe[line][column] == ".":
                list_cells.append((line, column))

    return list_cells


def cell_in_same_group(groups, cell_1, cell_2):
    if not groups:  # Check if the list is empty
        return False
    for sub_list in groups:
        if cell_1 in sub_list and cell_2 in sub_list:
            return True
    return False  # If no matching sublist is found with both values, return False


def merge_group(group, cell_1, cell_2):
    sublist1 = None
    sublist2 = None

    # Search for the sublists containing var1 and var2
    for sublist in group:
        if cell_1 in sublist:
            sublist1 = sublist
        if cell_2 in sublist:
            sublist2 = sublist

    # Merge the sublists if both are found and are distinct
    if sublist1 and sublist2 and sublist1 != sublist2:
        merged_sublist = list(set(sublist1 + sublist2))  # Merge and remove duplicates
        group.remove(sublist1)
        group.remove(sublist2)
        group.append(merged_sublist)

    return group


def valide(pos_neud_1, pos_neud_2, labyrinthe, groups):
    try:

        return labyrinthe[pos_neud_2[0]][pos_neud_2[1]] == "." and (
            not (cell_in_same_group(groups, pos_neud_1, pos_neud_2))
        )

    except:
        return False


def is_cell_in_group(groups, cell):
    for group in groups:
        for c in group:
            if cell == c:
                return True

    return False

def add_to_group(lst, target, new):
    for sub_list in lst:
        if target in sub_list:
            sub_list.append(new)
    return lst

def add_content_of_list_to_list (list_origin) :
    temp_list = []
    for item in list_origin :
        temp_list.append (item)

    return temp_list


def creat_labyrinthe(labyrinthe, n):
    list_cells = init_list_cells(labyrinthe, n)
    groups = []

    test_len = True
    while test_len :

        random.shuffle (list_cells)

        pos_neud_1 = list_cells[0]

        temp_direction = add_content_of_list_to_list (directions)

        random.shuffle(temp_direction)

        test = True
        
        while test and len(temp_direction) > 0:

            direction = temp_direction[0]

            pos_neud_2 = (pos_neud_1[0] + direction[0], pos_neud_1[1] + direction[1])

            print (groups)

            print (pos_neud_1)

            print (pos_neud_2)
            
            if valide(pos_neud_1, pos_neud_2, labyrinthe, groups):

                print ("test  2")


                if is_cell_in_group(groups, pos_neud_1) and is_cell_in_group(groups, pos_neud_2):

                    print ("test 3")

                    groups = merge_group(groups, pos_neud_1, pos_neud_2)
                    labyrinthe[pos_neud_1[0] + direction[0] // 2][pos_neud_1[1] + direction[1] // 2] = char_empty
                    test = False

                elif is_cell_in_group(groups, pos_neud_1) or is_cell_in_group(groups, pos_neud_2):

                    print ("test 4")

                    if is_cell_in_group(groups, pos_neud_1):
                        groups = add_to_group(groups, pos_neud_1, pos_neud_2)
                    else:
                        groups = add_to_group(groups, pos_neud_2, pos_neud_1)
                    
                    labyrinthe[pos_neud_1[0] + direction[0] // 2][pos_neud_1[1] + direction[1] // 2] = char_empty
                    test = False

                else:

                    print ("test 5")

                    groups.append([pos_neud_1, pos_neud_2])
                    labyrinthe[pos_neud_1[0] + direction[0] // 2][pos_neud_1[1] + direction[1] // 2] = char_empty
                    test = False

            temp_direction.pop(0)

        if len(temp_direction) == 0:
            list_cells.pop (0)
            temp_direction = add_content_of_list_to_list (directions)
        if len (list_cells) == 0 :
            test_len = False
     
    print("fin")


def entree_sortie(labyrinthe, n):
    labyrinthe[0][0] = char_empty
    labyrinthe[n - 1][n - 1] = char_empty
    labyrinthe[1][0] = char_empty
    labyrinthe[n - 2][n - 1] = char_empty



def generer_labyrinthe(n):
    labyrinthe = init_labyrinthe(n)
    creat_labyrinthe(labyrinthe, n)
    entree_sortie(labyrinthe, n)

    return labyrinthe


def sauvegarder_labyrinthe(labyrinthe, nom_fichier):
    with open(nom_fichier + ".txt", "w") as f:
        for ligne in labyrinthe:
            f.write("".join(ligne) + "\n")


def main():
    n = 2 * int(input("Entrez la taille du labyrinthe (n): ")) + 1
    nom_fichier = input("Entrez le nom du fichier de sortie: ")

    labyrinthe = generer_labyrinthe(n)

    sauvegarder_labyrinthe(labyrinthe, nom_fichier)
    print(f"Labyrinthe généré et sauvegardé dans {nom_fichier}.")


if __name__ == "__main__":
    main()
