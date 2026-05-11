





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Bool  {

    private String boolType;





    private robotDSL_Action robotdsl_action;




    private robotDSL_Trigger robotdsl_trigger;


    public robotDSL_Bool(
        String boolType    ) {
        this.boolType = boolType;
    }


    public String getBooltype() {
        return boolType;
    }

    public void setBooltype(String boolType) {
        this.boolType = boolType;
    }

    public robotDSL_Action getRobotdsl_action() {
        return robotdsl_action;
    }

    public void setRobotdsl_action(robotDSL_Action robotdsl_action) {
        this.robotdsl_action = robotdsl_action;
    }
    public robotDSL_Trigger getRobotdsl_trigger() {
        return robotdsl_trigger;
    }

    public void setRobotdsl_trigger(robotDSL_Trigger robotdsl_trigger) {
        this.robotdsl_trigger = robotdsl_trigger;
    }

}