





import java.util.List;
import java.util.ArrayList;

public class robot_Condition  {






    private robot_While robot_while;




    private robot_Event robot_event;




    private robot_Whenever robot_whenever;




    private robot_Alternative robot_alternative;


    public robot_Condition(
    ) {
    }



    public robot_While getRobot_while() {
        return robot_while;
    }

    public void setRobot_while(robot_While robot_while) {
        this.robot_while = robot_while;
    }
    public robot_Event getRobot_event() {
        return robot_event;
    }

    public void setRobot_event(robot_Event robot_event) {
        this.robot_event = robot_event;
    }
    public robot_Whenever getRobot_whenever() {
        return robot_whenever;
    }

    public void setRobot_whenever(robot_Whenever robot_whenever) {
        this.robot_whenever = robot_whenever;
    }
    public robot_Alternative getRobot_alternative() {
        return robot_alternative;
    }

    public void setRobot_alternative(robot_Alternative robot_alternative) {
        this.robot_alternative = robot_alternative;
    }

}