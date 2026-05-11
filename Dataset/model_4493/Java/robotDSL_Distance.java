





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Distance  {

    private int distance;





    private robotDSL_Trigger robotdsl_trigger;




    private robotDSL_Bool robotdsl_bool;


    public robotDSL_Distance(
        int distance    ) {
        this.distance = distance;
    }


    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    public robotDSL_Trigger getRobotdsl_trigger() {
        return robotdsl_trigger;
    }

    public void setRobotdsl_trigger(robotDSL_Trigger robotdsl_trigger) {
        this.robotdsl_trigger = robotdsl_trigger;
    }
    public robotDSL_Bool getRobotdsl_bool() {
        return robotdsl_bool;
    }

    public void setRobotdsl_bool(robotDSL_Bool robotdsl_bool) {
        this.robotdsl_bool = robotdsl_bool;
    }

}