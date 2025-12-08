---
name: "Feature: Per-Block Color Customization"
about: Allow users to choose colors for each block's background and patchwork independently
title: "feat: Add per-block color customization"
labels: enhancement, feature
assignees: ''
---

## Description

Currently, users can only choose one background color and one patchwork color for the entire quilt. This feature will allow users to customize the background and patchwork colors for each individual block.

## User Story

As a quilt designer, I want to choose different colors for each block's background and patchwork so that I can create more complex, multi-color quilt designs.

## Acceptance Criteria

- [ ] User can specify background color for each block (16 total)
- [ ] User can specify patchwork color for each block (16 total)
- [ ] Colors are validated against Tkinter color names
- [ ] User is prompted for colors in logical order (row by row, column by column)
- [ ] Quilt canvas displays each block with its custom colors
- [ ] All existing tests pass with new functionality
- [ ] New tests added for per-block color validation (target: 70%+ coverage)

## Implementation Notes

- Modify `QuiltUI.get_block_color_input()` to prompt for colors per block
- Update `BlockDrawer` methods to accept color parameter per block
- Store block colors in a data structure (e.g., 4x4 dictionary or list)
- Update `design_row()` to pass block-specific colors to drawing functions

## Testing Requirements

- Unit tests for color input per block
- Integration tests for full workflow with custom colors
- Edge cases: invalid colors, case sensitivity

## Related Issues

- Depends on: Refactoring complete (Phase 2)

