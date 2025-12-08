---
name: "Feature: Additional Block Patterns"
about: Add new quilt block patterns (Flying Geese, etc.) to expand design options
title: "feat: Add additional quilt block patterns"
labels: enhancement, feature
assignees: ''
---

## Description

Extend Patch.py with additional classic quilt block patterns beyond the current four. This allows users to create more diverse and interesting quilt designs.

## User Story

As a quilt designer, I want access to more classic quilt block patterns so that I can create more varied and interesting quilt designs.

## Acceptance Criteria

- [ ] At least 3 new block patterns implemented
- [ ] Each pattern has drawing function in `BlockDrawer`
- [ ] Each pattern has position options (if applicable)
- [ ] New patterns added to `AVAILABLE_QUILT_BLOCKS` config
- [ ] Position options added to `BLOCK_POSITIONS` config
- [ ] All existing tests pass with new patterns
- [ ] New tests added for each block pattern (target: 70%+ coverage)
- [ ] Documentation updated with new patterns

## Suggested Block Patterns

### Flying Geese
- **Description**: Three vertical triangles pointing in one direction
- **Positions**: Up, Down, Left, Right
- **Difficulty**: Medium

### Log Cabin
- **Description**: Concentric rectangles around a center square
- **Positions**: None (fixed pattern)
- **Difficulty**: Medium

### Nine Patch
- **Description**: 3x3 grid of smaller squares
- **Positions**: None (configurable via colors)
- **Difficulty**: Easy

### Pinwheel
- **Description**: Four triangles arranged in rotating pattern
- **Positions**: 4 rotations
- **Difficulty**: Medium

## Implementation Notes

- Add new block to `config.py`:
  ```python
  AVAILABLE_QUILT_BLOCKS = [
      "one patch",
      "four patch",
      "half square triangle",
      "quarter square triangle",
      "flying geese",  # NEW
      "log cabin",     # NEW
      # ...
  ]
- Add positions to BLOCK_POSITIONS:
  ```python
  BLOCK_POSITIONS = {
    # ...
    "flying geese": ["up", "down", "left", "right"],
    "log cabin": [],  # No positions
    # ...
  }
- Implement drawing methods in BlockDrawer:
  ```python
  @staticmethod
  def draw_flying_geese(canvas, start_x, start_y, color, direction):
      # Implementation
- Update design_row() in main.py to handle new patterns

## Testing Requirements

- Unit tests for each new block pattern
- Visual verification: Draw each pattern and verify appearance
- Integration tests with new patterns in full quilt design
- Edge cases: position validation for each pattern

## Related Issues

Depends on: Refactoring complete (Phase 2)
Related to: GUI Interface feature (optional)
