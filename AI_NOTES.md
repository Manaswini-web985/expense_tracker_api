# AI_NOTES.md

## AI Usage

I used ChatGPT as a development assistant during this project.

AI helped me with:
- Designing the Flask REST API structure.
- Creating route patterns for expense operations.
- Implementing JSON file storage and retrieval logic.
- Suggesting test cases for API endpoints.
- Improving error handling and input validation.

## Code Written vs AI-Assisted

### AI-assisted parts:
- Initial Flask route structure suggestions.
- JSON storage helper function ideas.
- Suggestions for API response formats.
- Test case ideas.

### Written and modified by me:
- Project structure setup.
- Implementation of expense CRUD operations.
- Integration of routes with storage functions.
- Validation of API behavior.
- Manual testing and debugging.

## Validation and Changes Made

After using AI suggestions, I:
- Reviewed and understood the generated code before using it.
- Added validation for missing required fields.
- Improved JSON file handling to avoid errors when the file is empty or corrupted.
- Tested all API endpoints manually using Postman.
- Verified that the application works correctly after restarting the server.

## AI Suggestions Not Used

AI suggested using a database layer for storing expenses, but I did not implement it because the assignment explicitly allowed in-memory storage or local JSON storage.

I chose JSON storage because it keeps the application simple, lightweight, and easy to run for evaluation.