from django.test import TestCase, Client
from django.urls import reverse, resolve
from ..views import HomePageView
from django.views.generic import TemplateView
from model_bakery import baker

test_data_items_number = 5


def create_test_data(items_number):
    sectors = baker.make("stocks.Sectors", _quantity=items_number)
    industries = baker.make(
        "stocks.Industries", sector=sectors[0], _quantity=items_number
    )
    tickers = baker.make(
        "stocks.Tickers", industry=industries[0], _quantity=items_number
    )
    return (sectors, industries, tickers)


class HomePageViewTests(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.url = reverse("home")
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_homepage_status_code(self):
        # print('HomePage Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_status_code_post(self):
        # print('HomePage Internal status code - post method')
        self.response_post = self.client.post("")
        self.assertEqual(self.response_post.status_code, 405)  # method not allowed

    def test_homepage_template(self):
        # print('HomePage template')
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html_title(self):
        # print('HomePage Internal title')
        self.assertContains(self.response, "Stocks and Sectors Data")

    def test_homepage_contains_correct_html_body(self):
        # print('HomePage Internal body')
        self.assertContains(
            self.response,
            "Here you can choose stocks for long and short positions in your portfolio, based on Forward P/E, Leverage, Margin, Liquidity",
        )

    def test_homepage_does_not_contain_incorrect_html(self):
        # print('HomePage Internal not contains')
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):
        # print('HomePage Internal homepage view name')
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()


class AboutPageViewTests(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.url = reverse("about")
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_aboutpage_status_code(self):
        # print('AboutPage Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_status_code_post(self):
        # print('AboutPage Internal status code - post method')
        self.response_post = self.client.post("/about/")
        self.assertEqual(self.response_post.status_code, 405)  # method not allowed

    def test_aboutpage_template(self):
        # print('AboutPage template')
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html_title(self):
        # print('AboutPage Internal title')
        self.assertContains(self.response, "About this site")

    def test_aboutpage_contains_correct_html_body(self):
        # print('AboutPage Internal body')
        self.assertContains(
            self.response,
            "Hello! Thank you for visiting this page. On this site, you can pre-select stocks and sectors for long and short positions in your investment portfolio, using the following",
        )

    def test_aboutpage_does_not_contain_incorrect_html(self):
        # print('AboutPage Internal not contains')
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_aboutpage_url_resolves_homepageview(self):
        # print('AboutPage Internal homepage view name')
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, TemplateView.as_view().__name__)

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()


class SearchViewTests(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # print('Search Page setup class')
        self.sectors, self.industries, self.tickers = create_test_data(
            test_data_items_number
        )
        # print(self.tickers[0].ticker[0:3])
        self.url = "{0}{1}{2}".format(
            reverse("search_results"), "?q=", self.tickers[0].ticker[0:3]
        )
        self.client = Client()
        self.response = self.client.get(self.url)
        # print(self.url)

    def test_search_status_code(self):
        # print('Search Page Internal status code - get method')

        # import inspect
        # attributes = inspect.getmembers(self.response, lambda a:not(inspect.isroutine(a)))
        # attributes_filtered = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        # print()
        # print(attributes_filtered)
        # print()

        self.assertEqual(self.response.status_code, 200)

    def test_search_status_code_post(self):
        # print('Search Page Internal status code - post method')
        self.response_post = self.client.post(self.url)
        self.assertEqual(self.response_post.status_code, 405)  # method not allowed

    def test_search_page_template(self):
        # print('Search Page template')
        self.assertTemplateUsed(self.response, "search_results.html")

    def test_search_contains_correct_html_title(self):
        # print('Search Page Internal title')
        self.assertContains(self.response, "<title>Search</title>")

    def test_search_contains_correct_html_body(self):
        # print('Search Page Internal body')
        self.assertContains(
            self.response,
            '<h1>Search Results</h1>\n<p>Search term: "{0}"</p>'.format(
                self.tickers[0].ticker[0:3]
            ),
        )

    def test_search_not_contains_incorrect_html(self):
        # print('Search Page Internal not contains')
        self.assertNotContains(self.response, "Hello World")

    def test_search_url_resolves_search_view(self):
        # print('Search Page Internal view name')
        view = resolve("/search/")
        self.assertEqual(view.func.__name__, "SearchResultsListView")

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()


class SectorDetailViewTests(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # print('SectorDetailViewTests setup class')
        self.sectors, self.industries, self.tickers = create_test_data(
            test_data_items_number
        )
        self.url = reverse("sectordetail", args=(self.sectors[0].slug,))
        # print(self.url)
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_sector_detail_status_code(self):
        # print('Sector detail Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)

    def test_sector_detail_status_code_post(self):
        # print('Sector detail Internal status code - post method')
        self.response_post = self.client.post(self.url)
        self.assertEqual(self.response_post.status_code, 405)  # method not allowed

    def test_sector_detail_contains_correct_html_title(self):
        # print('Sector detail Internal title')
        self.assertContains(
            self.response,
            "<title>{0} Sectors Industries Data</title>".format(self.sectors[0].sector),
        )

    def test_sector_detail_contains_correct_html_body(self):
        # print('Sector detail Internal body')
        self.assertContains(
            self.response,
            "<h1>{0} Sectors Industries Data</h1>".format(self.sectors[0].sector),
        )

    def test_sector_detail_not_contains_incorrect_html(self):
        # print('Sector detail Internal not contains')
        self.assertNotContains(self.response, "Hello World")

    def test_sector_detail_url_resolves_sector_detail_view(self):
        # print('Sector detail Internal view name')
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, "SectorDetailView")

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()


class IndustryDetailViewTests(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # print('IndustryDetailViewTests setup class')
        self.sectors, self.industries, self.tickers = create_test_data(
            test_data_items_number
        )
        self.url = reverse("industrydetail", args=(self.industries[0].slug,))
        # print(self.url)
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_industry_detail_status_code(self):
        # print('Industry detail Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)

    def test_industry_detail_status_code_post(self):
        # print('Industry detail Internal status code - post method')
        self.response_post = self.client.post(self.url)
        self.assertEqual(self.response_post.status_code, 405)  # method not allowed

    def test_industry_detail_contains_correct_html_title(self):
        # print('Industry detail Internal title')
        self.assertContains(
            self.response,
            "<title>{0} Industry Companies Data</title>".format(
                self.industries[0].industry
            ),
        )

    def test_industry_detail_contains_correct_html_body(self):
        # print('Industry detail Internal body')
        self.assertContains(
            self.response,
            "<h1>{0} Companies Data</h1>".format(self.industries[0].industry),
        )

    def test_industry_detail_not_contains_incorrect_html(self):
        # print('Industry detail Internal not contains')
        self.assertNotContains(self.response, "Hello World")

    def test_industry_detail_url_resolves_industry_detail_view(self):
        # print('Industry detail Internal view name')
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, "IndustryDetailView")

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()


class CompanyDetailViewTests(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # print('IndustryDetailViewTests setup class')
        self.sectors, self.industries, self.tickers = create_test_data(
            test_data_items_number
        )
        self.url = reverse("companydetail", args=(self.tickers[0].ticker,))
        # print(self.url)
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_company_detail_status_code(self):
        # print('Company detail Internal status code - get method')
        self.assertEqual(self.response.status_code, 200)

    def test_company_detail_status_code_post(self):
        # print('Company detail Internal status code - post method')
        self.response_post = self.client.post(self.url)
        self.assertEqual(self.response_post.status_code, 405)  # method not allowed

    def test_company_detail_contains_correct_html_title(self):
        # print('Company detail Internal title')
        self.assertContains(
            self.response,
            "<title>{0} Company Data</title>".format(self.tickers[0].ticker),
        )

    def test_company_detail_contains_correct_html_body(self):
        # print('Company detail Internal body')
        self.assertContains(
            self.response,
            "<h1>{0} None Company Data</h1>".format(self.tickers[0].ticker),
        )

    def test_company_detail_not_contains_incorrect_html(self):
        # print('Company detail Internal not contains')
        self.assertNotContains(self.response, "Hello World")

    def test_company_detail_url_resolves_company_detail_view(self):
        # print('Company detail Internal view name')
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, "CompanyDetailView")

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
