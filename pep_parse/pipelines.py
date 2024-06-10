import datetime as dt
from pathlib import Path


BASE_DIR = Path('../results/')


class PepParsePipeline:
    pep_status_count = {}

    def open_spider(self, spider):
        results_dir = Path(BASE_DIR)
        results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        status = item['status']

        if status not in self.pep_status_count:
            self.pep_status_count[status] = 0

        self.pep_status_count[status] += 1
        return item

    def close_spider(self, spider):
        create_date = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_path = BASE_DIR / f'status_summary_{create_date}.csv'

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in self.pep_status_count.items():
                f.write(f'{status},{count}\n')
            f.write(f'Total,{sum(self.pep_status_count.values())}')
