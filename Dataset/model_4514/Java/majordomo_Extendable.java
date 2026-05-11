





import java.util.List;
import java.util.ArrayList;

public class majordomo_Extendable  {






    private List<majordomo_Sensor> majordomo_sensors;




    private majordomo_Sensor majordomo_sensor;




    private majordomo_Actor majordomo_actor;




    private List<majordomo_Actor> majordomo_actors;


    public majordomo_Extendable(
    ) {
        this.majordomo_sensors = new ArrayList<>();
        this.majordomo_actors = new ArrayList<>();
    }

    public majordomo_Extendable(
        ArrayList<majordomo_Sensor> majordomo_sensors,        ArrayList<majordomo_Actor> majordomo_actors    ) {
        this.majordomo_sensors = majordomo_sensors;
        this.majordomo_actors = majordomo_actors;
    }


    public List<majordomo_Sensor> getMajordomo_sensors() {
        return majordomo_sensors;
    }

    public void addMajordomo_sensor(Majordomo_sensor majordomo_sensor) {
        this.majordomo_sensors.add(majordomo_sensor);
    }
    public majordomo_Sensor getMajordomo_sensor() {
        return majordomo_sensor;
    }

    public void setMajordomo_sensor(majordomo_Sensor majordomo_sensor) {
        this.majordomo_sensor = majordomo_sensor;
    }
    public majordomo_Actor getMajordomo_actor() {
        return majordomo_actor;
    }

    public void setMajordomo_actor(majordomo_Actor majordomo_actor) {
        this.majordomo_actor = majordomo_actor;
    }
    public List<majordomo_Actor> getMajordomo_actors() {
        return majordomo_actors;
    }

    public void addMajordomo_actor(Majordomo_actor majordomo_actor) {
        this.majordomo_actors.add(majordomo_actor);
    }

}