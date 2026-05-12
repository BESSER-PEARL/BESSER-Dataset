





import java.util.List;
import java.util.ArrayList;

public class Detect_Movement_external  {






    private Movement_Sensor_Actor movement_sensor_actor;




    private Door_Sensor_Actor door_sensor_actor;




    private Window_Sensor_Actor window_sensor_actor;


    public Detect_Movement_external(
    ) {
    }



    public Movement_Sensor_Actor getMovement_sensor_actor() {
        return movement_sensor_actor;
    }

    public void setMovement_sensor_actor(Movement_Sensor_Actor movement_sensor_actor) {
        this.movement_sensor_actor = movement_sensor_actor;
    }
    public Door_Sensor_Actor getDoor_sensor_actor() {
        return door_sensor_actor;
    }

    public void setDoor_sensor_actor(Door_Sensor_Actor door_sensor_actor) {
        this.door_sensor_actor = door_sensor_actor;
    }
    public Window_Sensor_Actor getWindow_sensor_actor() {
        return window_sensor_actor;
    }

    public void setWindow_sensor_actor(Window_Sensor_Actor window_sensor_actor) {
        this.window_sensor_actor = window_sensor_actor;
    }

}