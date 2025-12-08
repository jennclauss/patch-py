---
name: "Feature: Save/Load Quilt Designs"
about: Persist quilt designs to JSON; load previous designs from file
title: "feat: Add save/load quilt design functionality"
labels: enhancement, feature
assignees: ''
---

## Description

Allow users to save their quilt designs to a JSON file and load previously saved designs. This enables users to preserve their work and iterate on designs over time.

## User Story

As a quilt designer, I want to save my quilt designs to a file so that I can load and modify them later without having to redesign from scratch.

## Acceptance Criteria

- [ ] User can save quilt design to JSON file
- [ ] JSON includes: background color, patchwork colors, block designs, block positions
- [ ] User can load quilt design from JSON file
- [ ] Loaded design displays correctly on canvas
- [ ] File format is human-readable and documented
- [ ] Error handling for missing/corrupted files
- [ ] All existing tests pass with new functionality
- [ ] New tests added for save/load (target: 70%+ coverage)

## Implementation Notes

- Create `QuiltDesign` class to represent a quilt
  - Properties: background_color, blocks (list of block configs)
  - Methods: `to_json()`, `from_json()`
- Create `QuiltStorage` class for file I/O
  - Methods: `save_design(design, filepath)`, `load_design(filepath)`
- JSON schema:
  ```json
  {
    "version": "1.0",
    "background_color": "red",
    "blocks": [
      {
        "row": 0,
        "column": 0,
        "design": "one patch",
        "position": null,
        "color": "blue"
      }
    ]
  }
- Update main.py to offer save/load options after design completion

## Testing Requirements

- Unit tests for QuiltDesign serialization/deserialization
- Unit tests for QuiltStorage file operations
- Integration tests for full save/load workflow
- Edge cases: missing files, corrupted JSON, invalid designs

## Related Issues

Depends on: Feature - Per-Block Color Customization (optional)