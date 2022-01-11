import pytest
from pyppeteer import launch

@pytest.mark.asyncio
async def test_title():
    res = await test_h1()
    assert 'Shorturl' == res

@pytest.mark.asyncio
async def test_shorten_url():
    res = await go_to_url_then_return_page_url()
    assert res == 'https://dmdespert.com/'

async def test_h1():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://polr.stationmyr.net/')
    element = await page.querySelector("h1")
    title = await page.evaluate('(element) => element.textContent', element)
    await browser.close()
    return title

async def input_url_in_shorten_url():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://polr.stationmyr.net/')
    await page.type('[name="link-url"]', 'https://dmdespert.com/')
    await page.click("#shorten")
    element = await page.querySelector('#short_url')
    result = await page.evaluate("(element) => element.value", element)
    await browser.close()
    return result

async def go_to_url_then_return_page_url():
    browser = await launch()
    page = await browser.newPage()
    url = await input_url_in_shorten_url()
    await page.goto(url)
    result = page.url
    await browser.close()
    return result