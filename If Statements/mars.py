visit_mars = input("Would you like to visit Mars? [y/n] ")
want_to_go = visit_mars == "y"

affordable_trip = input("Can you afford to go to Mars? [y/n ")
can_afford = affordable_trip == "y"

can_go_to_mars = want_to_go and can_afford

print(f"You can go to Mars: {can_go_to_mars}")
