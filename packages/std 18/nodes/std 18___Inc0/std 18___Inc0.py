from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node


# GENERAL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output

# EDITING
# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(output or index)
# self.update_shape()                  <- recomputes the whole shape and content positions

# LOGGING
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')


class Inc_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(Inc_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        if configuration:
            self.set_data(configuration['state data'])


    def updating(self, token, input_called=-1):
        if input_called == 0:
            var_name = self.input(1)
            new_val = self.flow.parent_script.get_var(self.input(1)).val + 1
            self.flow.parent_script.set_var(var_name, new_val)
            self.outputs[1].set_val(new_val)
            self.exec_output(0)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass



    # optional - important for threading - stop everything here
    def removing(self):
        pass