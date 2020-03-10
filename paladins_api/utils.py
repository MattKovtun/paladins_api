from datetime import datetime, timedelta


def time_stamp(implicit=False):
    if implicit:
        return datetime.now().strftime("%Y%m%d")
    # you might need to adjust timedelta according to your timezone
    return (datetime.now() - timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
