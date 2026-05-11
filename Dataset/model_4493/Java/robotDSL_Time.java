





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Time  {

    private int sec;





    private robotDSL_Goal robotdsl_goal;


    public robotDSL_Time(
        int sec    ) {
        this.sec = sec;
    }


    public int getSec() {
        return sec;
    }

    public void setSec(int sec) {
        this.sec = sec;
    }

    public robotDSL_Goal getRobotdsl_goal() {
        return robotdsl_goal;
    }

    public void setRobotdsl_goal(robotDSL_Goal robotdsl_goal) {
        this.robotdsl_goal = robotdsl_goal;
    }

}