def check_lane_departure(l1, l2, img_width):
    mid_x = img_width // 2
    left_lane_x = (l1[0] + l1[2]) // 2
    right_lane_x = (l2[0] + l2[2]) // 2
    lane_center = (left_lane_x + right_lane_x) // 2

    if abs(mid_x - lane_center) > 50:  # Threshold for departure
        warning_text = "Lane Departure!"
        color = (0, 0, 255)
    else:
        warning_text = "In Lane"
        color = (0, 255, 0)

    return warning_text, color
