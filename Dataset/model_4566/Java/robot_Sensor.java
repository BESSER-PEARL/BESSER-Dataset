





import java.util.List;
import java.util.ArrayList;

public class robot_Sensor extends SensoryDevice {

    private int throttle;





    private robot_Sensor robot_sensor;


    public robot_Sensor(
        int throttle    ) {
        super(
        );
        this.throttle = throttle;
    }


    public int getThrottle() {
        return throttle;
    }

    public void setThrottle(int throttle) {
        this.throttle = throttle;
    }

    public robot_Sensor getRobot_sensor() {
        return robot_sensor;
    }

    public void setRobot_sensor(robot_Sensor robot_sensor) {
        this.robot_sensor = robot_sensor;
    }

}