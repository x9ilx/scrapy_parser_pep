import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path('results/')


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_status_count = defaultdict(lambda: 0)
        results_dir = Path(BASE_DIR)
        results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        status = item['status']
        self.pep_status_count[status] += 1
        return item

    def close_spider(self, spider):
        create_date = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_path = BASE_DIR / f'status_summary_{create_date}.csv'
        self.pep_status_count['Total'] = sum(self.pep_status_count.values())

        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Статус', 'Количество'))
            writer.writerows(self.pep_status_count.items())
