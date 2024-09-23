from src.model.types_and_stuff import transpose

# Returns n rotations of the sorted ordering of a given n-sized set

def rotations(pc_set):
    rotations = []
    sorted_set = sorted(pc_set)
    for index in range(len(sorted_set)):
        rotations.append(sorted_set[index:] + sorted_set[:index])
    return rotations


# Returns all of the intervals from the first pc in each rotation to every other
# pc int the set

def all_intervals(rotations):
    all_intervals = []
    for rotation in rotations:
        intervals = []
        moving_index = 1
        for _ in range(len(rotation) - 1):
            interval = rotation[len(rotation) - moving_index] - rotation[0]
            if interval < 0:
                intervals.append(interval + 12)
            else:
                intervals.append(interval)
            moving_index += 1
        all_intervals.append([rotation, intervals])
    return all_intervals

# Returns the best rotation

def best(intervals):
    counter = 0 
    while len(intervals) > 1:
        intervals_to_check = sorted([intervals[i][1][0] for i in range(len(intervals))])
        smallest = intervals_to_check[0]
        to_remove = []
        for j in range(len(intervals)):
            if intervals[j][1][0] != smallest:
                to_remove.append(intervals[j]) # Removes rotations that aren't
            else:                              # candidates for normal order
                pass
        if to_remove != []:
            for k in to_remove:
                intervals.remove(k)
        else:
            pass
        if len(intervals[0][1]) > 1: # Ensures all intervals aren't deleted
            for l in range(len(intervals)):
                del intervals[l][1][0]
        else:
            pass
        counter += 1
        if counter > 10: # This creates an exit condition for highly-symmetrical sets
            sorted_sets = sorted([intervals[m][0] for m in range(len(intervals))])
            return sorted_sets[0] # Chooses the set with the smallest first pc
    return intervals[0][0] # Returns the only remaining set after all ineligable
                           # rotations have been deleted


# Combines the above functions into a single function

def normal_order(pc_set):
    return best(all_intervals(rotations(pc_set)))
    
def is_reduced(pcset):
    return normal_order(pcset)[0] == 0
