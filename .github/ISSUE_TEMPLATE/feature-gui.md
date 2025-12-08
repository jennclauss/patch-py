---
name: "Feature: GUI Interface"
about: Build graphical interface (Tkinter or web-based) while keeping drawing and validation logic unchanged
title: "feat: Add GUI interface for quilt design"
labels: enhancement, feature, major
assignees: ''
---

## Description

Replace the terminal-based UI with a graphical user interface. This can be implemented using Tkinter (desktop) or a web framework (Flask/Django). The refactored code structure allows UI replacement without changing drawing or validation logic.

## User Story

As a quilt designer, I want a graphical interface so that I can design quilts more intuitively with visual feedback and mouse interactions.

## Acceptance Criteria

- [ ] GUI displays canvas with quilt design in real-time
- [ ] Color picker for background and patchwork colors
- [ ] Block design selector (dropdown or buttons)
- [ ] Position selector for blocks that require it
- [ ] Visual grid showing 4x4 block layout
- [ ] Save/load design buttons
- [ ] All existing drawing and validation logic unchanged
- [ ] All existing tests pass without modification
- [ ] New GUI tests added (target: 70%+ coverage)

## Implementation Notes

### Option A: Tkinter Desktop GUI
- Create `src/patch/gui_tkinter.py` with `QuiltGUI` class
- Inherit from `tk.Tk` or use `tk.Frame`
- Reuse `BlockDrawer`, `BlockValidator`, `QuiltUI` logic
- Canvas widget for quilt display
- Dropdown menus for color/design selection
- Grid layout for 4x4 block preview

### Option B: Web GUI (Flask)
- Create `src/patch/gui_web.py` with Flask app
- HTML/CSS/JavaScript frontend
- REST API endpoints for design operations
- Real-time canvas updates with WebSockets
- Responsive design for mobile/tablet

### Architecture
src/patch/ ├── config.py (unchanged) ├── validator.py (unchanged) ├── blocks.py (unchanged) ├── ui.py (terminal UI - unchanged) ├── gui_tkinter.py (NEW - graphical UI) └── main.py (updated to support both UIs)


## Testing Requirements

- Unit tests for GUI components (if possible)
- Integration tests for design workflow via GUI
- Manual testing: color selection, block design, canvas display
- Cross-platform testing (Mac, Windows, Linux)

## Related Issues

- Depends on: All previous features (optional)
- Blocks: Additional block patterns feature (optional)

## Resources

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Flask Documentation](https://flask.palletsprojects.com/)

