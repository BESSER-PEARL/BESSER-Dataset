





import java.util.List;
import java.util.ArrayList;

public class robotDSL_ArmOp  {

    private String opType;





    private robotDSL_Action robotdsl_action;


    public robotDSL_ArmOp(
        String opType    ) {
        this.opType = opType;
    }


    public String getOptype() {
        return opType;
    }

    public void setOptype(String opType) {
        this.opType = opType;
    }

    public robotDSL_Action getRobotdsl_action() {
        return robotdsl_action;
    }

    public void setRobotdsl_action(robotDSL_Action robotdsl_action) {
        this.robotdsl_action = robotdsl_action;
    }

}