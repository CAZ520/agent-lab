for score in [95, 85, 75, 55]:
    if score >= 90:
        print(f"{score}分，优秀")
    elif score >= 80:
        print(f"{score}分，良好")
    elif score >= 60:
        print(f"{score}分，及格")
    else:
        print(f"{score}分，不及格")
