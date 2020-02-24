
class Principal:
    def __init__(self, username, fullname):
      self.username = username
      self.fullname = fullname

    def __str__(self):
        return self.username

class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = []
        self.principals = []

    def __str__(self):
        principals_str = "["
        for p in self.principals:
            principals_str += p.username + ", "
        principals_str += "]"
        return "%s, %s" % (self.name, principals_str)

role_dev = Role("dev")
role_dev.permissions.append("release#create")
role_dev.principals.append(Principal("tjf", "Tim Fleming"))
role_dev.principals.append(Principal("one", "Emp ONe"))

role_qa = Role("qa")
role_qa.permissions.append("release#create")
role_qa.principals.append(Principal("one", "Emp ONe"))

role_prod = Role("prod")
role_prod.permissions.append("release#create")
role_prod.principals.append(Principal("one", "Emp ONe"))

roles = []
roles.append(role_dev)
roles.append(role_qa)
roles.append(role_prod)

user_roles = {}
print("START =============================")
for role in roles:
    print("\nrole: %s" % role)
    for principal in role.principals:
        print("  principal: %s" % principal.username)
        if principal.username in user_roles:
            print("    appending role '%s' for '%s'\n" % (role.name, principal.username))
            user_roles[principal.username].append(role.name)
        else:
            print("    adding role '%s' for '%s'\n" % (role.name, principal.username))
            user_roles[principal.username] = [role.name]

print(user_roles)
