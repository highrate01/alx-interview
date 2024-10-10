#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid) -> int:
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (List[List[int]]): A 2D list representing the island and water.
                            0 represents water, 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides for each land cell

                # Check adjacent cells and subtract shared sides
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2  # Subtract 2 for top neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2  # Subtract 2 for left neighbor

    return perimeter
