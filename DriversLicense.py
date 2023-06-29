def getTime(name,agents,other_customers): 
        wait_line = others.split() #
        wait_line.append(name)
        wait_line = sorted(wait_line)
        x = wait_line.index(name) + 1
        groups = 0
        while x >0:
            x-=agents
            groups+=1
        wait_time = 20*groups #It takes 20 minutes for each agent to create a license for a customer
        return wait_time
person = input()
workers = int(input())
others = input()
print(getTime(person,workers,others))
