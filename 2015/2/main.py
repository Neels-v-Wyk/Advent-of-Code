f = open("input", "r").readlines()
f = list(map(lambda s:s.strip(),f)) # strip newlines from each element

total_surface_area = 0
total_ribbon = 0

for boxes in f:
    
    dimensions = boxes.split('x')

    wlh = [int(dimensions[0]), int(dimensions[1]), int(dimensions[2])]

    w = wlh[0]
    l = wlh[1]
    h = wlh[2]

    wlh = [w, l, h]
    wlh.sort() # ensure smallest two sides are first

    ribbon_wrap = 2*(wlh[0]+wlh[1])
    ribbon_bow = w*l*h
    total_ribbon = total_ribbon + ribbon_wrap + ribbon_bow

    wl = 2*w*l
    wh = 2*w*h
    lh = 2*l*h

    individual_surfaces = [wl, wh, lh]
    individual_surfaces.sort() # ensure smallest element is always first


    surface_area = 3*individual_surfaces[0]/2 + individual_surfaces[1] + individual_surfaces[2]
    # 3*individual_surfaces[0]/2
    # x + x/2 = 3x/2
    # account for the fact that the smallest side is already *2 by dividing one surface by 2

    total_surface_area = total_surface_area + surface_area

print(total_surface_area)
print(total_ribbon)