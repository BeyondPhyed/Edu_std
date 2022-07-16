from vpython import *
#Web VPython 3.2

colors = [color.red, color.orange, color.yellow, color.green, color.blue, color.purple, color.magenta]
obj = sphere(color = color.cyan, radius = 0.2, emissive = True)
attach_light(obj)
rings = []

for i in range(7) : 
    rings.append(ring(pos = vec(i,0,0), color = colors[i]))

while True :
    rate(100)
    k = keysdown()
    if 'right' in k : 
        obj.pos.x += 0.05
    if 'left' in k:
        obj.pos.x -= 0.05
    if 'down' in k: 
        obj.pos.y -= 0.05
    if 'up' in k:
        obj.pos.y += 0.05
    if 'z' in k : 
        obj.pos.z += 0.05
    if 'x' in k : 
        obj.pos.z -= 0.05
        
    for i in range(len(rings)) : 
        if mag(obj.pos - rings[i].pos) <= 0.5 : 
            rings[i].color = obj.color
        else :
            rings[i].color = colors[i]
    
