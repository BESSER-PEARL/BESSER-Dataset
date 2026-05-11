





import java.util.List;
import java.util.ArrayList;

public class robot_Command extends MotoringDevice {

    private int id;





    private robot_Event robot_event;




    private robot_Command robot_command;


    public robot_Command(
        int id    ) {
        super(
        );
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public robot_Event getRobot_event() {
        return robot_event;
    }

    public void setRobot_event(robot_Event robot_event) {
        this.robot_event = robot_event;
    }
    public robot_Command getRobot_command() {
        return robot_command;
    }

    public void setRobot_command(robot_Command robot_command) {
        this.robot_command = robot_command;
    }

}