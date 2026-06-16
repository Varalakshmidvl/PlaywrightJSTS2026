# Chapter 3: Identifiers & Literals

## Overview
This chapter covers JavaScript identifier naming rules, naming conventions, and VS Code keyboard shortcuts.

## Files

| File | Description | Status |
|------|-------------|--------|
| `06_identifier_Rulers.js` | Basic identifier rules and examples | Completed |
| `07_identifier_part2.js` | Naming conventions (all cases) | Completed |
| `08_comments.js` | Comments and documentation (placeholder) | Completed |
| `js_identifier_rules.js` | Comprehensive identifier rules with examples | Completed |
| `vs_code_Keyboard_shortcuts_windows.js` | VS Code shortcuts reference | Completed |

## What We Learned

### 06_identifier_Rulers.js
- Valid identifiers: `$`, `_a`, `p`, `ab123`, `Name`, `name`, `pramod_dutta`, `pramod$dutta`
- Invalid (commented out): `123` (cannot start with digit), `pramod dutta` (no spaces)
- JavaScript is case-sensitive: `Name` and `name` are different

### 07_identifier_part2.js
Naming conventions in JavaScript:
1. **camelCase** - `userName`, `totalPrice`, `isLoggedIn` (standard for variables/functions)
2. **PascalCase** - `UserProfile`, `ShoppingCart` (standard for classes/constructors)
3. **snake_case** - `user_name`, `total_price` (valid but less common in JS)
4. **SCREAMING_SNAKE_CASE** - `MAX_SIZE`, `API_KEY` (standard for constants)
5. **Hungarian Notation** - `strName`, `bActive`, `nCount` (older style, rarely used now)

### js_identifier_rules.js
- Must begin with letter, underscore, or dollar sign
- Subsequent characters may include digits
- Cannot start with a digit
- Cannot be reserved keywords
- Case-sensitive language
- Unicode letters and escape sequences allowed
- Cannot contain spaces, hyphens, or special characters

### vs_code_Keyboard_shortcuts_windows.js
- Complete VS Code keyboard shortcuts for Windows
- Categories: General, Editing, Navigation, Search, Multi-cursor, Editor, Display, Debug, Terminal
- Customization with `Ctrl + K Ctrl + S`

## How to Run
```bash
node chapter_03_Identifiers_Literals/06_identifier_Rulers.js
node chapter_03_Identifiers_Literals/07_identifier_part2.js
node chapter_03_Identifiers_Literals/js_identifier_rules.js
```

## Next Chapter
Chapter 4: JavaScript Concepts (Variables, Scope, Hoisting) - Deep dive into var, let, const, and hoisting
