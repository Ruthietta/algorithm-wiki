# Quadtree Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** Depends on implementation
- **Requires:** A dataset of points

## Description

Quadtree Search is an algorithm used for searching multidimensional data, such as points in a 2D or 3D space. It divides the space recursively into quadrants (in 2D) or octants (in 3D) until the desired data is found or a certain threshold is reached.

## Algorithm

The Quadtree Search algorithm works as follows:

1. Divide the space into quadrants (in 2D) or octants (in 3D).
2. If the desired data lies entirely within one quadrant or octant, recursively search within that quadrant or octant.
3. If the desired data intersects multiple quadrants or octants, recursively search within each intersecting quadrant or octant.
4. Continue dividing and searching until the desired data is found or the search space cannot be divided further.
