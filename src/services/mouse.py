from pynput.mouse import Button, Controller


class Mouse(Controller):
    def drag(self, start_x, start_y, end_x, end_y):
        self.position = (start_x, start_y)
        self.press(Button.left)
        self.position = (end_x, end_y)
        self.release(Button.left)
