import sublime, sublime_plugin

class MoveTabLeftCommand(sublime_plugin.WindowCommand):
    def run(self):
        active_view = self.window.active_view()
        active_group = self.window.active_group()
        views_in_active_group = len(self.window.views_in_group(active_group))
        # get_view_index returns a tuple, `(group, index)`, we only care for
        # the index.
        active_view_index = self.window.get_view_index(active_view)[1]

        # This really could be a nasty one-liner, but I'm not a fan of those so
        # I've broken it out into it's constituent pieces.
        self.window.set_view_index(active_view, active_group,
            ((active_view_index -1 ) % views_in_active_group))


class MoveTabRightCommand(sublime_plugin.WindowCommand):
    def run(self):
        active_view = self.window.active_view()
        active_group = self.window.active_group()
        views_in_active_group = len(self.window.views_in_group(active_group))
        # get_view_index returns a tuple, `(group, index)`, we only care for
        # the index.
        active_view_index = self.window.get_view_index(active_view)[1]

        self.window.set_view_index(active_view, active_group,
            ((active_view_index + 1) % views_in_active_group))
