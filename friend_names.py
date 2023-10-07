invitation_list = ["gokhan","zafer","oguzhan"]
print(f"Dear {invitation_list[0].title()}, you invited to dinner.")
print(f"Dear {invitation_list[1].title()}, you invited to dinner.")
print(f"Dear {invitation_list[2].title()}, you invited to dinner.")

invitation_list.remove("zafer")
invitation_list.append("sinan")
print(invitation_list)
print(f"Dear {invitation_list[2].title()}, you invited to dinner.")

invitation_list.insert(0,"kerem")
invitation_list.insert(1,"selcuk")
invitation_list.append("gizem")
print(invitation_list)
print(f"Dear {invitation_list[0].title()}, you invited to dinner.")
print(f"Dear {invitation_list[1].title()}, you invited to dinner.")
print(f"Dear {invitation_list[-1].title()}, you invited to dinner.")

invitation_list.remove("kerem")
invitation_list.remove("selcuk")
invitation_list.remove("sinan")
invitation_list.remove("gizem")
print(invitation_list)

print(len(invitation_list))