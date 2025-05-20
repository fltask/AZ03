from scrapy.exporters import CsvItemExporter

class CsvCustomDelimiter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        # здесь указываем нужный разделитель
        kwargs['delimiter'] = ';'
        # сохраняем остальные параметры
        super(CsvCustomDelimiter, self).__init__(*args, **kwargs)