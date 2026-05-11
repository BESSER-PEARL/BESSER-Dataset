





import java.util.List;
import java.util.ArrayList;

public class drone_TaskDescriptor  {






    private List<drone_AreaObject> drone_areaobjects;




    private drone_Task drone_task;




    private drone_Task drone_task;


    public drone_TaskDescriptor(
    ) {
        this.drone_areaobjects = new ArrayList<>();
    }

    public drone_TaskDescriptor(
        ArrayList<drone_AreaObject> drone_areaobjects    ) {
        this.drone_areaobjects = drone_areaobjects;
    }


    public List<drone_AreaObject> getDrone_areaobjects() {
        return drone_areaobjects;
    }

    public void addDrone_areaobject(Drone_areaobject drone_areaobject) {
        this.drone_areaobjects.add(drone_areaobject);
    }
    public drone_Task getDrone_task() {
        return drone_task;
    }

    public void setDrone_task(drone_Task drone_task) {
        this.drone_task = drone_task;
    }
    public drone_Task getDrone_task() {
        return drone_task;
    }

    public void setDrone_task(drone_Task drone_task) {
        this.drone_task = drone_task;
    }

}