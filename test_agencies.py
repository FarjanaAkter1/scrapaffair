import unittest
from unittest.mock import Mock

class Test_agencies(unittest.TestCase):
    def test_agency_titles(self, mock_bs, mock_get):
        mock_response = Mock()

        mock_response.content = '''<a href="https://www.consumeraffairs.com/travel/zicasso.html" 
        data-ga-data-layer="{&quot;campaign_id&quot;: 17200, &quot;gtm_event&quot;: &quot;brand-click&quot;}" 
        class="ca-a ca-a--bld-no-undln brd-card__tit-nm js-gadatalayer" data-track-goal="buyersguide:profile_entrances:click" 
        data-uapi-link="company_name_cta">
                    Zicasso
                </a>'''