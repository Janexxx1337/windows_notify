from win10toast import ToastNotifier


def windows_popup(title, content, duration=10):
    toast = ToastNotifier()
    toast.show_toast(title, content, duration=duration)
    

windows_popup('Доброе утро!', 'Вова!')
