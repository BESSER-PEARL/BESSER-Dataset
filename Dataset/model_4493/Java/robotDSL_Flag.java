





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Flag  {

    private String name;





    private robotDSL_Mission robotdsl_mission;




    private robotDSL_Trigger robotdsl_trigger;




    private robotDSL_Action robotdsl_action;


    public robotDSL_Flag(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public robotDSL_Mission getRobotdsl_mission() {
        return robotdsl_mission;
    }

    public void setRobotdsl_mission(robotDSL_Mission robotdsl_mission) {
        this.robotdsl_mission = robotdsl_mission;
    }
    public robotDSL_Trigger getRobotdsl_trigger() {
        return robotdsl_trigger;
    }

    public void setRobotdsl_trigger(robotDSL_Trigger robotdsl_trigger) {
        this.robotdsl_trigger = robotdsl_trigger;
    }
    public robotDSL_Action getRobotdsl_action() {
        return robotdsl_action;
    }

    public void setRobotdsl_action(robotDSL_Action robotdsl_action) {
        this.robotdsl_action = robotdsl_action;
    }

}