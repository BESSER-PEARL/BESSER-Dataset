





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Trigger  {

    private int degrees;
    private String touching;





    private robotDSL_Goal robotdsl_goal;


    public robotDSL_Trigger(
        int degrees,        String touching    ) {
        this.degrees = degrees;
        this.touching = touching;
    }


    public int getDegrees() {
        return degrees;
    }

    public void setDegrees(int degrees) {
        this.degrees = degrees;
    }
    public String getTouching() {
        return touching;
    }

    public void setTouching(String touching) {
        this.touching = touching;
    }

    public robotDSL_Goal getRobotdsl_goal() {
        return robotdsl_goal;
    }

    public void setRobotdsl_goal(robotDSL_Goal robotdsl_goal) {
        this.robotdsl_goal = robotdsl_goal;
    }

}