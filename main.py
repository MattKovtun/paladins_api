import pandas as pd
from datetime import timedelta

from paladins_api.match_api import MatchApi
from paladins_api.dev_creds import DEV_ID, AUTH_KEY

RANKED_SIEGE = './data/ranked_siege/'
RANKED_SIEGE_CODE = '486'


def scrap_ranked_matches(start_date, end_date):
    def scrap_match(date):
        data = api.get_match_ids_by_queue(RANKED_SIEGE_CODE, date, hour='-1', verbose=True)
        pp = RANKED_SIEGE + date

        with open(pp, 'w') as f:
            f.write(str(len(data)) + '\n')
            for line in data:
                f.write(line['Match'] + '\n')

    api = MatchApi(DEV_ID, AUTH_KEY)
    end_date = pd.to_datetime(end_date).date()
    date = pd.to_datetime(start_date).date()
    while date != end_date:
        print(date)
        scrap_match(date.strftime('%Y%m%d'))
        print()
        date += timedelta(days=1)


if __name__ == "__main__":
    # adjust date accordingly
    date = '20200308'
    end_date = '20200310'
    scrap_ranked_matches(date, end_date)
