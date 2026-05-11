





import java.util.List;
import java.util.ArrayList;

public class robot_Effector extends MotoringDevice {

    private int throttle;
    private int sustain;





    private robot_Effector robot_effector;




    private robot_Sensor robot_sensor;


    public robot_Effector(
        int throttle,        int sustain    ) {
        super(
        );
        this.throttle = throttle;
        this.sustain = sustain;
    }


    public int getThrottle() {
        return throttle;
    }

    public void setThrottle(int throttle) {
        this.throttle = throttle;
    }
    public int getSustain() {
        return sustain;
    }

    public void setSustain(int sustain) {
        this.sustain = sustain;
    }

    public robot_Effector getRobot_effector() {
        return robot_effector;
    }

    public void setRobot_effector(robot_Effector robot_effector) {
        this.robot_effector = robot_effector;
    }
    public robot_Sensor getRobot_sensor() {
        return robot_sensor;
    }

    public void setRobot_sensor(robot_Sensor robot_sensor) {
        this.robot_sensor = robot_sensor;
    }

}