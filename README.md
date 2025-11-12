# SauceDemo E2E Test Framework (v2: Keyword-Driven Architecture)

This is a complete redesign of the test automation project for the [SauceDemo](https://www.saucedemo.com/) website. It utilizes Playwright and Pytest, but shifts from a traditional Page Object Model (POM) to a scalable, **Keyword-Driven Testing (KDT)** architecture.

---

## 💡 Architecture & Key Features (Why v2 is Better)

This framework is built on the philosophy that **test cases should be data, not code**.

### 1. Keyword-Driven / Data-Driven Testing (KDT/DDT)

- **Decoupled Logic:** All complex test logic (e.g., filling fields, clicking buttons) is hidden inside dedicated Python functions (The "Lego Blocks").
- **JSON Test Pipelines:** Every test scenario is defined as a simple, human-readable pipeline of operations stored in `.json` files. The tests themselves are **never written in Python**.
- **Single Test Runner:** All 16+ test cases (Login, Inventory, E2E) are executed by a **single, highly parameterized Pytest function**, which iterates through all the JSON pipelines.

### 2. Pydantic-Validated Schema (Fail Fast)

- **Schema Enforcement:** Pydantic V2 is used to validate every JSON test pipeline before the browser even opens.
- **Instant Feedback:** Any typo in a keyword, missing parameter, or incorrectly structured test will fail instantly with a clear `ValidationError`, preventing slow failures deep within the test execution layer.

### 3. Maintainability & Scalability

- **Hidden Locators:** Test writers (even non-technical users) never need to see or interact with CSS selectors. Locators are abstracted and hidden within the dedicated operation files (`login_ops.py`, `inventory_ops.py`).
- **Modular Operations:** The framework is structured with granular operation files (`operations/operations/`) and model definition files (`operations/models/`) to ensure the Single Responsibility Principle (SRP) is enforced, making it easy to add new pages or keywords.

---

## What It Tests

This framework covers the main user flows of the SauceDemo site:

- **Login (10 Scenarios):** Runs 10 different data-driven scenarios from a JSON file (valid users, locked-out user, invalid credentials, blank fields).
- **Inventory (5 Scenarios):** Verifies all 4 product sorting options (A-Z, Z-A, Price Low-High, Price High-Low) and checks item-to-cart functionality.
- **End-to-End Checkout (1 Scenario):** A complete test that simulates a user logging in, adding an item to the cart, filling out checkout information, and successfully placing an order.

---

## Tech Stack

- **Language:** Python
- **Browser Automation:** Playwright
- **Test Runner:** Pytest
- **Data Modeling:** Pydantic V2
- **Reporting:** Allure Reports
- **CI/CD:** GitHub Actions

---

## How to Run Locally

1. **Clone the repository:**

   ```
   git clone https://github.com/AlShabiliBadia/saucedemo-playwright-e2e-V2
   cd saucedemo-playwright-e2e
   ```

2. **Set up a virtual environment:**

   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Install Playwright's browsers:**

   ```
   playwright install
   ```

5. **Run tests & generate Allure results:**

   ```
   python -m pytest --alluredir=allure-results --clean-alluredir
   ```

6. **Run a specific group of tests (using dynamic markers from the JSON data):**

   ```
   python -m pytest -m smoke
   python -m pytest -m "e2e and checkout"
   ```

7. **View the HTML report:**

   ```
   allure serve allure-results
   ```
