# Chapter 19: Playwright Basics

## Overview
This chapter covers the fundamentals of Playwright - a powerful automation framework for browser testing. It includes setup, basic commands, selectors, actions, and assertions.

## Files

| File | Description | Status |
|------|-------------|--------|
| *(Files to be added)* | Playwright setup and basic tests | Planned |

## What We Will Learn

### Setup
- Installing Playwright: `npm init playwright@latest`
- Project structure and configuration (`playwright.config.js`)
- Running tests: `npx playwright test`
- UI mode: `npx playwright test --ui`

### Core Concepts
- **Browsers**: Chromium, Firefox, WebKit support
- **Pages**: Interacting with browser tabs
- **Locators**: Finding elements robustly
- **Actions**: Click, fill, navigate, screenshot
- **Assertions**: Built-in auto-retrying assertions

### Example Test
```javascript
import { test, expect } from '@playwright/test';

test('basic navigation', async ({ page }) => {
    await page.goto('https://example.com');
    await expect(page).toHaveTitle(/Example/);
    await page.click('text=More information');
});
```

## Key Takeaways
- Playwright supports multiple browsers with a single API
- Auto-waiting and retrying makes tests reliable
- Codegen can generate tests from user actions: `npx playwright codegen`
- Trace viewer helps debug failing tests
- Fixtures provide clean setup/teardown

## Prerequisites
```bash
npm init playwright@latest
```

## How to Run
```bash
npx playwright test
npx playwright test --headed
npx playwright test --ui
```

## Previous Chapter
Chapter 18: Async Await
