#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Owner, Pet

fake = Faker() #initializing instance of Faker() to use. 

with app.app_context(): #create an application. ensures apps fail quickly if they are not configed with this.

    Pet.query.delete() #Model.query.delete(). Syntax change from vanilla SQLA. Session is managed through Flask so no need to call. 
    Owner.query.delete()

    owners = [] #Empty list to append fake instances
    for n in range(50): #For loop to define how many fakes we want to make
        owner = Owner(name=fake.name()) #fake instance. attr with fake.method()
        owners.append(owner) #append owners to list

    db.session.add_all(owners) #commit all to db. 

    pets = []
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    for n in range(100):
        pet = Pet(name=fake.name(), species=rc(species), owner=rc(owners))
        pets.append(pet)

    db.session.add_all(pets)

    db.session.commit() #commit all of the above.