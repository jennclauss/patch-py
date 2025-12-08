---
name: "Feature: Hex Color Code Support"
about: Support hex color codes (#RRGGBB and RRGGBB formats) with regex validation
title: "feat: Add hex color code support with validation"
labels: enhancement, feature
assignees: ''
---

## Description

Extend color input to support hex color codes in addition to Tkinter color names. This allows users to specify any RGB color using standard hex notation.

## User Story

As a quilt designer, I want to use hex color codes (like #FF5733 or FF5733) so that I can choose from a much wider range of colors beyond Tkinter's built-in palette.

## Acceptance Criteria

- [ ] Accept hex codes in format `#RRGGBB` (with hash)
- [ ] Accept hex codes in format `RRGGBB` (without hash)
- [ ] Validate hex codes using regular expressions
- [ ] Convert hex codes to Tkinter-compatible format (if needed)
- [ ] Maintain backward compatibility with Tkinter color names
- [ ] User can mix Tkinter colors and hex codes in same quilt
- [ ] All existing tests pass with new functionality
- [ ] New tests added for hex validation (target: 70%+ coverage)

## Implementation Notes

- Update `BlockValidator.validate_color()` to accept hex codes
- Implement regex pattern: `^#?[0-9A-Fa-f]{6}$`
- Create `BlockValidator.normalize_hex_color()` to standardize format
- Update UI prompts to mention hex code support
- Consider: Convert hex to RGB tuple for canvas compatibility

## Testing Requirements

- Unit tests for hex code validation
  - Valid: `#FF5733`, `FF5733`, `#000000`, `#ffffff`
  - Invalid: `#GGGGGG`, `#FF57`, `FF573`, `notahex`
- Integration tests with mixed color types
- Edge cases: case sensitivity, leading zeros

## Related Issues

- Depends on: Feature - Per-Block Color Customization (optional)

