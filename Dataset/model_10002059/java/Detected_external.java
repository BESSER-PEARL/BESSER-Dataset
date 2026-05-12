





import java.util.List;
import java.util.ArrayList;

public class Detected_external  {






    private Water_Sensor_Actor water_sensor_actor;




    private Heat_Sensor_Actor heat_sensor_actor;




    private Movement_Sensor_Actor movement_sensor_actor;


    public Detected_external(
    ) {
    }



    public Water_Sensor_Actor getWater_sensor_actor() {
        return water_sensor_actor;
    }

    public void setWater_sensor_actor(Water_Sensor_Actor water_sensor_actor) {
        this.water_sensor_actor = water_sensor_actor;
    }
    public Heat_Sensor_Actor getHeat_sensor_actor() {
        return heat_sensor_actor;
    }

    public void setHeat_sensor_actor(Heat_Sensor_Actor heat_sensor_actor) {
        this.heat_sensor_actor = heat_sensor_actor;
    }
    public Movement_Sensor_Actor getMovement_sensor_actor() {
        return movement_sensor_actor;
    }

    public void setMovement_sensor_actor(Movement_Sensor_Actor movement_sensor_actor) {
        this.movement_sensor_actor = movement_sensor_actor;
    }

}