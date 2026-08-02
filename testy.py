def morning_routine(is_hungry):
    print("Get up.")
    print("Do the bed.")
    print("Go to the bathroom.")
    print("Brush teeth.")
    print("Wash face.")
    print("Go downstairs.")

    if is_hungry:
        print("Eat breakfast.")
    else:
        print("Skip breakfast.")

    return "Morning routine done!"

morning_routine()