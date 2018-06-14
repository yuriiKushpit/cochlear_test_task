from element_data.element import View


class StartingView(View):
    def __init__(self):
        super().__init__()
        self.collect_elements()
