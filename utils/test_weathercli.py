import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:5000"


def test_page_loads(page: Page):
    """Test if page loads"""
    page.goto(BASE_URL)
    expect(page).to_have_title("Weather App")


def test_search_valid_city(page: Page):
    """Test searching for a valid city"""
    page.goto(BASE_URL)
    
    # Fill input and click button
    page.locator('input[name="city"]').fill("London")
    page.locator('button[type="submit"]').click()
    
    # Check weather card appears
    expect(page.locator('.card')).to_be_visible(timeout=10000)
    expect(page.locator('.card h3')).to_contain_text("London")


def test_search_invalid_city(page: Page):
    """Test searching for invalid city shows error"""
    page.goto(BASE_URL)
    
    page.locator('input[name="city"]').fill("InvalidCity123")
    page.locator('button[type="submit"]').click()
    
    # Check error message appears
    expect(page.locator('.error')).to_be_visible(timeout=10000)
    expect(page.locator('.error')).to_contain_text("City not found")


def test_form_elements_exist(page: Page):
    """Test form elements are present"""
    page.goto(BASE_URL)
    
    expect(page.locator('input[name="city"]')).to_be_visible()
    expect(page.locator('button[type="submit"]')).to_be_visible()