# coding: utf-8

'''Implémentation d'une pile.'''

def creer_pile():
    """ Cree une pile vide """
    return []

def pile_vide(pile):
    """ Retourne True si la pile est vide """
    return pile == []

def sommet(pile):
    """ Retourne le premier élément de la pile.
        Prduit une erreur si la pile est vide """
    assert not pile_vide(pile), 'sommet : pile vide!!'
    return pile[len(pile)-1]

def empiler(pile, element):
    """ Ajoute élément au sommet de la pile, et retourne la nouvelle pile """
    pile.append(element)
    return pile

def depiler(pile):
    """ Retire le premier élément de la pile et retourne la nouvelle pile
        Produit une erreur si la pile est vide """
    assert not pile_vide(pile), 'depiler : pile vide!!'
    tete = sommet(pile)
    pile.pop()
    return tete

def elements_pile(pile):
    """ Retourne un tableau Python contenant les éléments de la pile depuis le sommet """
    res = []
    for i in range(len(pile)-1, -1, -1):
        res.append(pile[i])
    return res
