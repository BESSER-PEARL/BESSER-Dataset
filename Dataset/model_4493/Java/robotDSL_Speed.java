





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Speed  {

    private String speed;





    private robotDSL_Action robotdsl_action;


    public robotDSL_Speed(
        String speed    ) {
        this.speed = speed;
    }


    public String getSpeed() {
        return speed;
    }

    public void setSpeed(String speed) {
        this.speed = speed;
    }

    public robotDSL_Action getRobotdsl_action() {
        return robotdsl_action;
    }

    public void setRobotdsl_action(robotDSL_Action robotdsl_action) {
        this.robotdsl_action = robotdsl_action;
    }

}