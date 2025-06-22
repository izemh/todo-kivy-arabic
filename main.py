
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.1, 1)

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: dp(20)
    spacing: dp(10)

    Label:
        text: "قائمة المهام"
        font_name: 'fonts/Cairo-Regular.ttf'
        font_size: '24sp'
        halign: 'right'
        size_hint_y: None
        height: self.texture_size[1]
        color: 1, 1, 1, 1
        text_size: self.width, None

    BoxLayout:
        spacing: dp(10)
        size_hint_y: None
        height: dp(50)

        TextInput:
            id: task_input
            hint_text: 'أضف مهمة جديدة'
            font_name: 'fonts/Cairo-Regular.ttf'
            font_size: '18sp'
            halign: 'right'
            multiline: False
            foreground_color: 1, 1, 1, 1
            background_color: 0.15, 0.15, 0.2, 1
            cursor_color: 1, 1, 1, 1

        Button:
            text: '➕'
            font_size: '20sp'
            on_press: app.add_task(task_input.text)
            background_color: 0.2, 0.6, 0.3, 1

    ScrollView:
        GridLayout:
            id: tasks_layout
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(5)

<TaskItem@BoxLayout>:
    task_text: ''
    size_hint_y: None
    height: dp(50)
    spacing: dp(10)

    CheckBox:
        on_active: root.parent.remove_widget(root) if self.active else None

    Label:
        text: root.task_text
        font_name: 'fonts/Cairo-Regular.ttf'
        font_size: '18sp'
        halign: 'right'
        text_size: self.width, None
        color: 1, 1, 1, 1
'''

class ToDoApp(App):
    def build(self):
        return Builder.load_string(KV)

    def add_task(self, text):
        text = text.strip()
        if text:
            task_item = Builder.template('TaskItem', task_text=text)
            self.root.ids.tasks_layout.add_widget(task_item)
            self.root.ids.task_input.text = ''

if __name__ == '__main__':
    ToDoApp().run()
