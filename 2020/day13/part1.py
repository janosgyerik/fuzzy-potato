#!/usr/bin/env python

import sys
from heapq import heappush


def read_lines(path):
    with open(path) as fh:
        return [line.rstrip() for line in fh.readlines()]


def parse_lines(lines):
    arrival = int(lines[0])
    schedule = lines[1].split(',')
    buses = [(int(x), offset) for offset, x in enumerate(schedule) if x != 'x']
    return arrival, buses


def find_next_bus(buses, arrival):
    heap = []
    for bus, _ in buses:
        div = arrival // bus + 1
        heappush(heap, (bus * div, bus))

    return heap[0]


def find_contest_timestamp(buses):
    candidate = 0
    increment = 1
    for bus, offset in buses:
        while (candidate + offset) % bus != 0:
            candidate += increment
        increment *= bus

    return candidate


def main():
    lines = read_lines(sys.argv[1])
    arrival, buses = parse_lines(lines)
    next_bus_time, next_bus_id = find_next_bus(buses, arrival)
    print((next_bus_time - arrival) * next_bus_id)
    print(find_contest_timestamp(buses))


if __name__ == '__main__':
    main()
