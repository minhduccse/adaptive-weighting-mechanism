def AverageDistancePerFrame(boids):

    dist_sum = 0
    pos = 1
    count = 0
    for boid in boids:
        for other_boid in boids[pos:]: 
            dist_sum += boid.pos.distance_to(other_boid.pos)
            count += 1
        pos += 1
    if count != 0:
        dist_sum /= count
        # print("average distance of frame: "+str(dist_sum))
        return dist_sum
    return 0 
