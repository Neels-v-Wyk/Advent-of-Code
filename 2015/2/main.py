f = open("input", "r").readlines()
f = list(map(lambda s:s.strip(),f)) # strip newlines from each element

total_surface_area = 0

for boxes in f:
    
    dimensions = boxes.split('x')

    wlh = [int(dimensions[0]), int(dimensions[1]), int(dimensions[2])]

    w = wlh[0]
    l = wlh[1]
    h = wlh[2]

    wl = 2*w*l
    wh = 2*w*h
    lh = 2*l*h

    individual_surfaces = [wl, wh, lh]
    individual_surfaces.sort() # make sure smallest element is always first
    print(individual_surfaces)

    surface_area = (2*individual_surfaces[0]) + individual_surfaces[1] + individual_surfaces[2]
    total_surface_area = total_surface_area + surface_area

print(total_surface_area)
