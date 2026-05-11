





import java.util.List;
import java.util.ArrayList;

public class robotDSL_Mission  {

    private String name;





    private robotDSL_Goal robotdsl_goal;




    private robotDSL_Missions robotdsl_missions;


    public robotDSL_Mission(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public robotDSL_Goal getRobotdsl_goal() {
        return robotdsl_goal;
    }

    public void setRobotdsl_goal(robotDSL_Goal robotdsl_goal) {
        this.robotdsl_goal = robotdsl_goal;
    }
    public robotDSL_Missions getRobotdsl_missions() {
        return robotdsl_missions;
    }

    public void setRobotdsl_missions(robotDSL_Missions robotdsl_missions) {
        this.robotdsl_missions = robotdsl_missions;
    }

}