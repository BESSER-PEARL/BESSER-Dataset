





import java.util.List;
import java.util.ArrayList;

public class iec61131_configurations_Fb_Task extends Prog_Conf_Element {






    private Task_Name task_name;




    private Variable_Name variable_name;


    public iec61131_configurations_Fb_Task(
    ) {
        super(
        );
    }



    public Task_Name getTask_name() {
        return task_name;
    }

    public void setTask_name(Task_Name task_name) {
        this.task_name = task_name;
    }
    public Variable_Name getVariable_name() {
        return variable_name;
    }

    public void setVariable_name(Variable_Name variable_name) {
        this.variable_name = variable_name;
    }

}