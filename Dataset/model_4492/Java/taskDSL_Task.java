





import java.util.List;
import java.util.ArrayList;

public class taskDSL_Task  {

    private String name;





    private taskDSL_Detector taskdsl_detector;




    private taskDSL_DSL taskdsl_dsl;




    private taskDSL_Action taskdsl_action;




    private taskDSL_Mission taskdsl_mission;


    public taskDSL_Task(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public taskDSL_Detector getTaskdsl_detector() {
        return taskdsl_detector;
    }

    public void setTaskdsl_detector(taskDSL_Detector taskdsl_detector) {
        this.taskdsl_detector = taskdsl_detector;
    }
    public taskDSL_DSL getTaskdsl_dsl() {
        return taskdsl_dsl;
    }

    public void setTaskdsl_dsl(taskDSL_DSL taskdsl_dsl) {
        this.taskdsl_dsl = taskdsl_dsl;
    }
    public taskDSL_Action getTaskdsl_action() {
        return taskdsl_action;
    }

    public void setTaskdsl_action(taskDSL_Action taskdsl_action) {
        this.taskdsl_action = taskdsl_action;
    }
    public taskDSL_Mission getTaskdsl_mission() {
        return taskdsl_mission;
    }

    public void setTaskdsl_mission(taskDSL_Mission taskdsl_mission) {
        this.taskdsl_mission = taskdsl_mission;
    }

}