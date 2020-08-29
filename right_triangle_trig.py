import math
import turtle
#import matplotlib.pyplot as plt
import numpy as np


def get_inputs(inputs):
    nums = {}
    if "1" in inputs:
        nums["adj_side"] = int(input("Adjacent Side Length = "))
    if "2" in inputs:
        nums["opp_side"] = int(input("Opposite Side Length = "))
    if "3" in inputs:
        nums['hyp'] = int(input("Hypotenuse Length = "))
    if "4" in inputs:
        nums['adj_angle'] = int(input("Adjacent Angle = "))
        if nums['adj_angle'] > 89:
            raise ValueError("Your input for Adjacent Angle isn't possible.")
    if "5" in inputs:
        nums['opp_angle'] = int(input("Opposite Angle = "))
        if nums['opp_angle'] > 89:
            raise ValueError("Your input for Opposite Angle isn't possible.")
    return nums


def adjside_oppside(nums):
    nums["hyp"] = round(math.sqrt(nums["adj_side"]**2 + nums["opp_side"]**2), 2)
    nums["adj_angle"] = round(math.degrees(math.atan(nums["opp_side"] / nums["adj_side"])), 2)
    nums["opp_angle"] = round(90 - nums["adj_angle"], 2)
    run_checks(nums)
    draw_triangle(nums)
    return nums


def adjside_hyp(nums):
    if "adj_side" in nums and "hyp" in nums:
        nums['opp_side'] = math.sqrt(nums['hyp']**2 - nums['adj_side']**2)
        nums['adj_angle'] = math.degrees(math.atan(nums['opp_side'] / nums['adj_side']))
        nums['opp_angle'] = 90 - nums['adj_angle']
        run_checks(nums)
        draw_triangle(nums)


def adjside_adjangle(nums):
    if "adj_side" in nums and "adj_angle" in nums:
        nums['opp_angle'] = 90 - nums['adj_angle']
        nums['opp_side'] = math.tan(math.radians(nums['adj_angle'])) * nums['adj_side']
        nums['hyp'] = math.sqrt(nums['adj_side']**2 + nums['opp_side']**2)
        run_checks(nums)
        draw_triangle(nums)


def adjside_oppangle(nums):
    if "adj_side" in nums and "opp_angle" in nums:
        nums['adj_angle'] = 90 - nums['opp_angle']
        nums['opp_side'] = math.tan(math.radians(nums['adj_angle'])) * nums['adj_side']
        nums['hyp'] = math.sqrt(nums['adj_side']**2 + nums['opp_side']**2)
        run_checks(nums)
        draw_triangle(nums)


def oppside_hyp(nums):
    if "opp_side" in nums and "hyp" in nums:
        nums['adj_side'] = math.sqrt(nums['hyp']**2 - nums['opp_side']**2)
        nums['adj_angle'] = math.degrees(math.atan(nums['opp_side'] / nums['adj_side']))
        nums['opp_angle'] = 90 - nums['adj_angle']
        run_checks(nums)
        draw_triangle(nums)


def oppside_adjangle(nums):
    if "opp_side" in nums and "adj_angle" in nums:
        nums['opp_angle'] = 90 - nums['adj_angle']
        nums['adj_side'] = nums['opp_side'] / math.tan(math.radians(nums['adj_angle']))
        nums['hyp'] = math.sqrt(nums['adj_side']**2 + nums['opp_side']**2)
        run_checks(nums)
        draw_triangle(nums)


def oppside_oppangle(nums):
    if "opp_side" in nums and "opp_angle" in nums:
        nums['adj_angle'] = 90 - nums['opp_angle']
        nums['adj_side'] = nums['opp_side'] / math.tan(math.radians(nums['adj_angle']))
        nums['hyp'] = math.sqrt(nums['adj_side']**2 + nums['opp_side']**2)
        run_checks(nums)
        draw_triangle(nums)


def hyp_adjangle(nums):
    if "hyp" in nums and "adj_angle" in nums:
        nums['opp_angle'] = 90 - nums['adj_angle']
        nums['adj_side'] = math.cos(math.radians(nums['adj_angle'])) * nums['hyp']
        nums['opp_side'] = math.sqrt(nums['hyp']**2 - nums['adj_side'])
        run_checks(nums)
        draw_triangle(nums)


def hyp_opp_angle(nums):
    if "hyp" in nums and "opp_angle" in nums:
        nums['adj_angle'] = 90 - nums['opp_angle']
        nums['adj_side'] = ""
        nums['opp_side'] = ""
        run_checks(nums)
        draw_triangle(nums)


def adjangle_oppangle(nums):
    if "adj_angle" in nums and "opp_angle" in nums:
        print("You need to chose at least one side.  ")
        exit()
    else:
        print("Error:  Invalid Selections")


def run_checks(checking):
    if 90 == (checking['adj_angle'] + checking['opp_angle']):
        pass
        #print(checking['adj_angle'])
        #print(checking['opp_angle'])
    else:
        print("CALCULATION ERROR 1")
        exit()
    if checking['hyp']**2 == checking['adj_side']**2 + checking ['opp_side']**2:
        pass
    else:
        print("CALCULATION ERROR 2")


def draw_triangle(numbers):
    print("RESULTS:")
    print(f"Adjacent Side Length = {numbers['adj_side']}")
    print(f"Opposite Side Length = {numbers['opp_side']}")
    print(f"Hypotenuse Length = {numbers['hyp']}")
    print(f"Adjacent Angle = {numbers['adj_angle']}")
    print(f"Opposite Angle = {numbers['opp_angle']}")
    tt = turtle.Turtle()
    tt.pensize(5)
    tt.color("blue")
    tt.forward(numbers['adj_side'])
    tt.left(180 - numbers['adj_angle'])
    tt.forward(numbers['hyp'])
    tt.left(180 - numbers['opp_angle'])
    tt.forward(numbers['opp_side'])
    turtle.done()

if __name__ == "__main__":
    menu = """
    *************************
    This is to calculate and draw the dimensions of a right triangle.

        5
        /|
    3 / |
    /  | 2
    /___|
    4  1

    Here are your options to input:
    1 - Adjacent side (x-axis)
    2 - Opposite side (y-axis)
    3 - Hypotenuse
    4 - Adjacent angle
    5 - Opposite angle
    *************************
    """
    print(menu)

    selections = []
    selections.append(input("First option: "))
    selections.append(input("Second option: "))

    if selections == ["4","5"]:
        raise ValueError("You need to chose at least one side of the triangle.")

    data = get_inputs(selections)

    if "adj_side" in data and "opp_side" in data:
        adjside_oppside(data)
    elif "adj_side" in data and "hyp" in data:
        adjside_hyp(data)
    elif "adj_side" in data and "adj_angle" in data:
        adjside_adjangle(data)
    elif "adj_side" in data and "opp_angle" in data:
        adjside_oppangle(data)
    elif "opp_side" in data and "hyp" in data:
        oppside_hyp(data)
    elif "opp_side" in data and "adj_angle" in data:
        oppside_adjangle(data)
    elif "opp_side" in data and "opp_angle" in data:
        oppside_oppangle(data)
    elif "hyp" in data and "adj_angle" in data:
        hyp_adjangle(data)
    elif "hyp" in data and "opp_angle" in data:
        hyp_oppangle(data)
    else:
        raise ValueError(f"Your selections '{selections[0]}' and '{selections[1]}' were invlaid.  Please choose the numbers of the options that you wish to select.")
