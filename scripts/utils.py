from scripts.constants import Vector2, Rect


def point_in_circle(point: Vector2, circle: Vector2, radius: int):
    return (circle - point).magnitude() <= radius


def point_in_rectangle(
    point: Vector2, rectangle_position: Vector2, rectangle_size: Vector2
):
    return (
        point.x >= rectangle_position.x - rectangle_size.x / 2
        and point.x <= rectangle_position.x + rectangle_size.x / 2
        and point.y >= rectangle_position.y - rectangle_size.y / 2
        and point.y <= rectangle_position.y + rectangle_size.y / 2
    )


def line_on_line(x1, y1, x2, y2, x3, y3, x4, y4):
    uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / (
        (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    )
    uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / (
        (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    )

    return uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1


def circle_on_rectangle(
    circle_position: Vector2,
    circle_radius,
    rectangle_position: Vector2,
    rectangle_size: Vector2,
):
    cx = circle_position.x
    cy = circle_position.y

    rx = rectangle_position.x - rectangle_size.x / 2
    ry = rectangle_position.y - rectangle_size.y / 2

    t_x, t_y = cx, cy

    if cx < rx:
        t_x = rx
    elif cx > rx + rectangle_size.x:
        t_x = rx + rectangle_size.x

    if cy < ry:
        t_y = ry
    elif cy > ry + rectangle_size.y:
        t_y = ry + rectangle_size.y

    return (
        t_x
        and t_y
        and (Vector2(t_x, t_y) - circle_position).magnitude() <= circle_radius
    )
