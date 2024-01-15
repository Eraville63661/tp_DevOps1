def ecrit(prenom, matiere):
    if len(prenom) == 0:
        prenom = 'Ryan'
    if len(matiere) == 0 :
        matiere = 'DevOps'

    print('Programme de : ' + str(prenom) + '\nEn cours de : ' + str(matiere))


# if __name__ == "__main__":
#     prenom = ''
#     matiere = ''
#     ecrit(prenom, matiere)