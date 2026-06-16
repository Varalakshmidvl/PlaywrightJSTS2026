#!/usr/bin/env python3
"""Generate a JavaScript Identifiers Reference PDF."""

import os
import sys

# Try to import FPDF, install if missing
try:
    from fpdf import FPDF
except ImportError:
    print("Installing required PDF library...")
    os.system(f"{sys.executable} -m pip install fpdf2 -q")
    from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(33, 37, 41)
        self.cell(0, 10, "JavaScript Identifiers - Complete Reference", ln=True, align="C")
        self.ln(2)
        self.set_draw_color(0, 123, 255)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(0, 123, 255)
        self.cell(0, 8, title, ln=True)
        self.ln(1)

    def body_text(self, text, bold_terms=None):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 37, 41)
        if bold_terms:
            # Simple bold injection by splitting on terms
            lines = text.split("\n")
            for line in lines:
                self.set_x(10)
                if not line.strip():
                    self.ln(4)
                    continue
                self.set_font("Helvetica", "", 10)
                self.multi_cell(0, 5, line)
            self.ln(2)
        else:
            self.multi_cell(0, 5, text)
            self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 37, 41)
        self.cell(5, 5, chr(149), ln=0)  # bullet
        self.multi_cell(0, 5, text)
        self.ln(1)

    def code_block(self, lines, label=""):
        if label:
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(108, 117, 125)
            self.cell(0, 5, label, ln=True)
        self.set_fill_color(248, 249, 250)
        self.set_draw_color(222, 226, 230)
        self.set_font("Courier", "", 9)
        self.set_text_color(33, 37, 41)
        for line in lines:
            self.cell(0, 5, "  " + line, ln=True, fill=True)
        self.ln(2)

    def rule_box(self, title, desc, ok_examples, bad_examples):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(0, 123, 255)
        self.cell(0, 6, title, ln=True)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(33, 37, 41)
        self.multi_cell(0, 5, desc)
        self.ln(1)
        if ok_examples:
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(40, 167, 69)
            self.cell(0, 5, "Valid:", ln=True)
            self.code_block(ok_examples)
        if bad_examples:
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(220, 53, 69)
            self.cell(0, 5, "Invalid:", ln=True)
            self.code_block(bad_examples)
        self.ln(2)


def main():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Intro
    pdf.chapter_title("What Is an Identifier?")
    pdf.body_text(
        "An identifier is a name you choose for variables, constants, functions, classes, "
        "object properties, and labels in JavaScript. Choosing valid and meaningful identifiers "
        "is essential for writing clean, maintainable code."
    )

    # Core Rules
    pdf.chapter_title("1. Core Syntax Rules")
    pdf.body_text(
        "JavaScript identifiers must follow these strict rules. Breaking any of them causes a "
        "SyntaxError."
    )

    pdf.rule_box(
        "Rule 1: Allowed Characters",
        "Identifiers can contain letters (A-Z, a-z), digits (0-9), underscore (_), and dollar sign ($). "
        "JavaScript also supports Unicode letters (e.g., e with acute, Chinese characters, Greek lambda).",
        ok_examples=[
            "let userName = \"Alice\";",
            "let _count = 0;",
            "let $button = document.querySelector('button');",
            "let total2 = 100;",
            "let unicodeVar = 42;   // Unicode letters are allowed",
        ],
        bad_examples=[
            "let user-name = 5;   // Hyphen not allowed (parsed as subtraction)",
            "let user name = 5;   // Space not allowed",
            "let user@name = 5;   // @ is not allowed",
            "let #tag = 5;        // # is not allowed",
        ],
    )

    pdf.rule_box(
        "Rule 2: Cannot Start with a Digit",
        "The first character must be a letter, underscore, or dollar sign. Starting with a digit is illegal.",
        ok_examples=[
            "let value2 = 10;",
            "let _2nd = 20;",
            "let $2nd = 30;",
            "let secondValue = 40;",
        ],
        bad_examples=[
            "let 2ndValue = 10;   // SyntaxError: Invalid or unexpected token",
            "let 123abc = 5;      // SyntaxError",
        ],
    )

    pdf.rule_box(
        "Rule 3: Case Sensitivity",
        "JavaScript identifiers are case-sensitive. userName, UserName, and USERNAME are three completely different identifiers.",
        ok_examples=[
            "let userName = 'Alice';",
            "let UserName = 'Bob';",
            "let USERNAME = 'Charlie';",
            "console.log(userName);  // 'Alice'",
            "console.log(UserName);  // 'Bob'",
        ],
        bad_examples=[
            "// There is no error here, but confusing names cause bugs",
            "let data = 1;",
            "let Data = 2;",
            "let DATA = 3;",
            "// Always use distinct, meaningful names instead.",
        ],
    )

    pdf.rule_box(
        "Rule 4: No Reserved Keywords",
        "You cannot use JavaScript reserved words as identifiers. Some are always reserved; others are reserved in strict mode or specific contexts.",
        ok_examples=[
            "let myClass = 'Economics';  // 'class' is reserved, but 'myClass' is fine",
            "let _if = true;            // Underscore prefix makes it valid",
            "let $return = 5;            // Dollar prefix makes it valid",
        ],
        bad_examples=[
            "let class = 10;     // SyntaxError: Unexpected token 'class'",
            "let return = 5;     // SyntaxError: Unexpected token 'return'",
            "let if = true;      // SyntaxError: Unexpected token 'if'",
            "let const = 1;      // SyntaxError: Unexpected token 'const'",
        ],
    )

    # Reserved words list
    pdf.add_page()
    pdf.chapter_title("2. Reserved Words (Forbidden Identifiers)")
    pdf.body_text(
        "The following words cannot be used as identifiers in any context. "
        "Using them will produce a SyntaxError immediately."
    )

    reserved = [
        "break", "case", "catch", "class", "const", "continue", "debugger", "default",
        "delete", "do", "else", "export", "extends", "finally", "for", "function",
        "if", "import", "in", "instanceof", "let", "new", "return", "super", "switch",
        "this", "throw", "try", "typeof", "var", "void", "while", "with", "yield",
    ]
    strict_reserved = [
        "enum", "await", "implements", "package", "protected", "static", "interface",
        "private", "public", "abstract", "boolean", "byte", "char", "double", "final",
        "float", "goto", "int", "long", "native", "short", "synchronized", "throws",
        "transient", "volatile",
    ]

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "Always Reserved (ECMAScript standard):", ln=True)
    pdf.set_font("Courier", "", 9)
    for i, word in enumerate(reserved):
        if i % 5 == 0:
            pdf.ln(1)
        pdf.cell(38, 5, word, ln=0)
    pdf.ln(6)

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "Reserved in Strict Mode or Specific Contexts:", ln=True)
    pdf.set_font("Courier", "", 9)
    for i, word in enumerate(strict_reserved):
        if i % 5 == 0:
            pdf.ln(1)
        pdf.cell(38, 5, word, ln=0)
    pdf.ln(8)

    pdf.body_text(
        "Note: In strict mode, some additional words like 'let' and 'static' are also enforced. "
        "Modern modules and classes implicitly run in strict mode."
    )

    # Naming conventions
    pdf.add_page()
    pdf.chapter_title("3. Naming Conventions (Best Practices)")
    pdf.body_text(
        "While JavaScript allows many identifier styles, the community follows strong conventions "
        "for readability and consistency."
    )

    conventions = [
        (
            "camelCase",
            "Variables, functions, methods, and object properties",
            [
                "let userName = 'Alice';",
                "function getUserData() { ... }",
                "const calculateTotal = () => ...;",
                "let firstName = 'John';",
            ],
        ),
        (
            "PascalCase",
            "Classes, constructors, and React/Vue components",
            [
                "class UserProfile { ... }",
                "class ShoppingCart { ... }",
                "function MyComponent() { ... }",
                "class DataProcessor { ... }",
            ],
        ),
        (
            "SCREAMING_SNAKE_CASE",
            "Constants and configuration values",
            [
                "const MAX_SIZE = 100;",
                "const API_URL = 'https://api.example.com';",
                "const DEFAULT_TIMEOUT = 5000;",
                "const PI = 3.14159;",
            ],
        ),
        (
            "snake_case",
            "Sometimes used in object keys or legacy code; less common in modern JS",
            [
                "let user_name = 'Alice';  // Valid but not preferred",
                "const api_key = 'abc';    // Valid but camelCase is preferred",
            ],
        ),
    ]

    for name, usage, examples in conventions:
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(0, 123, 255)
        pdf.cell(0, 6, f"{name}", ln=True)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(108, 117, 125)
        pdf.cell(0, 5, f"Usage: {usage}", ln=True)
        pdf.code_block(examples)
        pdf.ln(2)

    # Special prefixes
    pdf.add_page()
    pdf.chapter_title("4. Special Prefix Meanings")
    pdf.body_text(
        "While not enforced by the language, certain prefixes carry conventional meaning "
        "in JavaScript codebases."
    )

    prefixes = [
        (
            "Underscore (_) prefix",
            "Often indicates a 'private' or internal member. It is a convention only - "
            "JavaScript does not enforce true privacy with a single underscore.",
            [
                "class Counter {",
                "  _count = 0;          // intended as private",
                "  _increment() { ... } // intended as private",
                "}",
            ],
        ),
        (
            "Double underscore (__) prefix",
            "Rarely used in user code. Some frameworks use it for internal utilities. "
            "Avoid using this in your own identifiers to prevent confusion.",
            [
                "// Example from frameworks (not user code)",
                "// React uses __SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED",
            ],
        ),
        (
            "Dollar sign ($) prefix",
            "Historically associated with jQuery or DOM element references. "
            "Still common in code that manipulates DOM nodes directly.",
            [
                "const $button = document.querySelector('#submit');",
                "const $input = document.getElementById('name');",
                "const $modal = $('.modal'); // jQuery-style",
            ],
        ),
    ]

    for title, desc, examples in prefixes:
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(0, 123, 255)
        pdf.cell(0, 6, title, ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(33, 37, 41)
        pdf.multi_cell(0, 5, desc)
        pdf.ln(1)
        pdf.code_block(examples)
        pdf.ln(2)

    # Complete examples table
    pdf.add_page()
    pdf.chapter_title("5. Complete Valid vs Invalid Examples")
    pdf.body_text(
        "The table below covers every common scenario you will encounter when naming identifiers in JavaScript."
    )

    examples_data = [
        ("userName", "Valid", "Standard camelCase variable"),
        ("UserName", "Valid", "PascalCase variable (allowed but usually for classes)"),
        ("user_name", "Valid", "snake_case is syntactically valid"),
        ("_count", "Valid", "Underscore prefix, internal-use convention"),
        ("$button", "Valid", "Dollar prefix, DOM element convention"),
        ("value2", "Valid", "Digits allowed after first character"),
        ("_2nd", "Valid", "Starts with underscore, contains digit"),
        ("$2nd", "Valid", "Starts with dollar, contains digit"),
        ("pi", "Valid", "Unicode letter (Greek pi) is valid"),
        ("unicodeVar", "Valid", "Unicode letter (Chinese) is valid"),
        ("lambda", "Valid", "Unicode letter (Greek lambda) is valid"),
        ("__proto__", "Valid", "Double underscore, special but valid"),
        ("2ndValue", "Invalid", "Cannot start with a digit"),
        ("123abc", "Invalid", "Cannot start with a digit"),
        ("user-name", "Invalid", "Hyphen is not allowed"),
        ("user name", "Invalid", "Space is not allowed"),
        ("user@name", "Invalid", "@ is not allowed"),
        ("#tag", "Invalid", "# is not allowed"),
        ("user.name", "Invalid", "Dot is not allowed in a simple identifier"),
        ("class", "Invalid", "Reserved keyword"),
        ("return", "Invalid", "Reserved keyword"),
        ("if", "Invalid", "Reserved keyword"),
        ("const", "Invalid", "Reserved keyword"),
        ("let", "Invalid", "Reserved keyword"),
        ("function", "Invalid", "Reserved keyword"),
        ("true", "Invalid", "Reserved literal (boolean)"),
        ("false", "Invalid", "Reserved literal (boolean)"),
        ("null", "Invalid", "Reserved literal"),
        ("undefined", "Valid", "Not a reserved word, but avoid using as variable name"),
        ("NaN", "Valid", "Global property, not a reserved word, but avoid reassigning"),
        ("Infinity", "Valid", "Global property, not a reserved word, but avoid reassigning"),
    ]

    # Table header
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(0, 123, 255)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(50, 7, "Identifier", border=1, fill=True, align="C")
    pdf.cell(30, 7, "Status", border=1, fill=True, align="C")
    pdf.cell(110, 7, "Explanation", border=1, fill=True, align="C")
    pdf.ln(7)

    for name, status, explanation in examples_data:
        if status == "Valid":
            pdf.set_text_color(40, 167, 69)
        else:
            pdf.set_text_color(220, 53, 69)
        pdf.set_font("Courier", "B", 9)
        pdf.cell(50, 6, name, border=1, align="L")
        pdf.cell(30, 6, status, border=1, align="C")
        pdf.set_text_color(33, 37, 41)
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(110, 6, explanation, border=1, align="L")
        pdf.ln(6)

    pdf.ln(4)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(108, 117, 125)
    pdf.multi_cell(
        0,
        5,
        "Note: Even if an identifier is syntactically valid, it may be a bad practice to use it. "
        "For example, reassigning 'undefined' or 'NaN' can cause subtle bugs even though the parser allows it.",
    )

    # Common mistakes
    pdf.add_page()
    pdf.chapter_title("6. Common Mistakes & How to Fix Them")

    mistakes = [
        (
            "Using hyphens in variable names",
            "JavaScript interprets hyphens as the subtraction operator.",
            ["let user-name = 'Alice';  // SyntaxError"],
            ["let userName = 'Alice';   // Correct"],
        ),
        (
            "Starting with a number",
            "The parser expects an identifier to start with a non-digit character.",
            ["let 2ndPlace = 'silver';  // SyntaxError"],
            ["let secondPlace = 'silver';  // Correct", "let _2ndPlace = 'silver';    // Also correct"],
        ),
        (
            "Using spaces inside identifiers",
            "Spaces separate tokens in JavaScript.",
            ["let user name = 'Alice';  // SyntaxError"],
            ["let userName = 'Alice';   // Correct", "let user_name = 'Alice';  // Also correct"],
        ),
        (
            "Shadowing reserved words without meaning to",
            "Accidentally naming a variable 'class' or 'let' inside a function.",
            ["function demo() { let class = 'A'; }  // SyntaxError"],
            ["function demo() { let className = 'A'; }  // Correct"],
        ),
        (
            "Case confusion when importing/exporting",
            "A module exports 'myData' but you import 'MyData'.",
            ["// Module A: export const myData = 1;", "// Module B: import { MyData } from './A';  // Error: MyData not found"],
            ["// Module B: import { myData } from './A';  // Correct"],
        ),
    ]

    for title, desc, bad, good in mistakes:
        pdf.set_font("Helvetica", "B", 11)
        pdf.set_text_color(0, 123, 255)
        pdf.cell(0, 6, title, ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(33, 37, 41)
        pdf.multi_cell(0, 5, desc)
        pdf.ln(1)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(220, 53, 69)
        pdf.cell(0, 5, "Wrong:", ln=True)
        pdf.code_block(bad)
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(40, 167, 69)
        pdf.cell(0, 5, "Right:", ln=True)
        pdf.code_block(good)
        pdf.ln(2)

    # Quick reference
    pdf.add_page()
    pdf.chapter_title("7. Quick Reference Checklist")
    pdf.body_text("Before you use an identifier, run through this checklist:")

    checklist = [
        "Does it start with a letter, underscore (_), or dollar sign ($)?",
        "Does it contain only letters, digits, underscore, or dollar sign?",
        "Is it NOT a reserved keyword (e.g., let, class, return, if)?",
        "Is it descriptive and meaningful (e.g., totalPrice instead of x)?",
        "Does it follow the project's naming convention (camelCase / PascalCase / SCREAMING_SNAKE_CASE)?",
        "Is it not too similar to another identifier in the same scope (case-sensitive)?",
        "Are you avoiding reassigning global properties like undefined, NaN, or Infinity?",
    ]

    for item in checklist:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(0, 123, 255)
        pdf.cell(6, 6, "[]", ln=0)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(33, 37, 41)
        pdf.multi_cell(0, 6, item)
        pdf.ln(1)

    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(33, 37, 41)
    pdf.cell(0, 8, "Summary", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(
        0,
        5,
        "Valid identifiers in JavaScript start with a letter, underscore, or dollar sign, contain only "
        "allowed characters, avoid reserved words, and follow consistent naming conventions. "
        "When in doubt, use camelCase for variables and functions, PascalCase for classes, and "
        "SCREAMING_SNAKE_CASE for constants.",
    )

    # Output
    output_path = r"C:\PWAutomation\Playwright2XMay2026\JavaScript_Identifiers_Reference.pdf"
    pdf.output(output_path)
    print(f"PDF created successfully at: {output_path}")


if __name__ == "__main__":
    main()
