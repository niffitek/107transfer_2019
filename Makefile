##
## EPITECH PROJECT, 2019
## d
## File description:
## h
##

NAME	    =	    107transfer

PYNAME	    =	    src/main.py

all:
	    cp $(PYNAME) $(NAME)
	    chmod 777 $(NAME)

fclean:	    clean
	    rm $(NAME)

re:	    fclean all

clean:
	    touch lol
	    rm lol
