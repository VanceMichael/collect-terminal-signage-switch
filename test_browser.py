"""在 Chromium 中核对柜台的实际可见控件及回执。"""
import unittest

from playwright.sync_api import sync_playwright
from test_source import SourceTests


class BrowserDeskTests(unittest.TestCase):
    """从真实页面填写每个柜台已知的输入。"""

    @classmethod
    def setUpClass(cls):
        SourceTests.setUpClass()
        cls.addClassCleanup(SourceTests.tearDownClass)
        cls.runtime = sync_playwright().start()
        cls.addClassCleanup(cls.runtime.stop)
        cls.browser = cls.runtime.chromium.launch()
        cls.addClassCleanup(cls.browser.close)

    def test_visible_receipts(self):
        page = self.browser.new_page()
        self.addCleanup(page.close)
        for form in SourceTests.config["forms"]:
            for values, message in form["choices"]:
                with self.subTest(path=form["path"], values=values):
                    page.goto(SourceTests.url + form["path"])
                    for label, value in zip(form["fields"].values(), values, strict=True):
                        page.get_by_label(label, exact=True).fill(value)
                    page.get_by_role("button", name="办理").click()
                    result = page.locator("output")
                    self.assertTrue(result.is_visible())
                    self.assertEqual(result.inner_text(), message)
