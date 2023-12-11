with open('./input.txt', 'r') as r:
    data = r.readlines()

time = list(map(int, data[0].split(':', 1)[1].split()))
distance = list(map(int, data[1].split(':', 1)[1].split()))


def get_distance_traveled(charge_time, t):
    time_left = t - charge_time
    dist_traveled = time_left * charge_time
    # print(charge_time, t, time_left, dist_traveled)
    return dist_traveled


def part1(time, distance):
    answer = []
    for i in range(len(distance)):
        t, d = time[i], distance[i]
        # print(t, d)
        mx_time, mn_time = 0, 0
        for j in range(1, t):
            d_trav = get_distance_traveled(j, t)
            mn_time = j if d_trav > d else 0
            if mn_time != 0:
                # print(mn_time)
                break

        for j in range(t-1, 0, -1):
            d_trav = get_distance_traveled(j, t)
            mx_time = j if d_trav > d else 0
            if mx_time != 0:
                # print(mx_time)
                break

        ways = mx_time - mn_time + 1
        answer.append(ways)
        # break
    return answer


# ans = part1(time, distance)
# pdt = 1
# for i in ans:
#     pdt *= i
# print(pdt)

new_time = [int(''.join([str(i) for i in time]))]
new_distance = [int(''.join([str(i) for i in distance]))]

ans = part1(new_time, new_distance)
print(ans)

# print(time)
# print(distance)
