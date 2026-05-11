





import java.util.List;
import java.util.ArrayList;

public class robot_Event extends SensoryDevice {

    private int id;





    private robot_Event robot_event;


    public robot_Event(
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

}