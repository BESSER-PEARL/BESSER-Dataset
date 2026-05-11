





import java.util.List;
import java.util.ArrayList;

public class robo_Setup  {






    private List<robo_Sensor> robo_sensors;




    private robo_Robot robo_robot;


    public robo_Setup(
    ) {
        this.robo_sensors = new ArrayList<>();
    }

    public robo_Setup(
        ArrayList<robo_Sensor> robo_sensors    ) {
        this.robo_sensors = robo_sensors;
    }


    public List<robo_Sensor> getRobo_sensors() {
        return robo_sensors;
    }

    public void addRobo_sensor(Robo_sensor robo_sensor) {
        this.robo_sensors.add(robo_sensor);
    }
    public robo_Robot getRobo_robot() {
        return robo_robot;
    }

    public void setRobo_robot(robo_Robot robo_robot) {
        this.robo_robot = robo_robot;
    }

}