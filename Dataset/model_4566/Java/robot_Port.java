





import java.util.List;
import java.util.ArrayList;

public class robot_Port extends ChannelDevice {

    private String mode;





    private robot_Port robot_port;


    public robot_Port(
        String mode    ) {
        super(
        );
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public robot_Port getRobot_port() {
        return robot_port;
    }

    public void setRobot_port(robot_Port robot_port) {
        this.robot_port = robot_port;
    }

}