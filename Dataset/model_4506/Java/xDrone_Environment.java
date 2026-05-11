





import java.util.List;
import java.util.ArrayList;

public class xDrone_Environment  {






    private List<xDrone_Object> xdrone_objects;




    private List<xDrone_Walls> xdrone_wallss;




    private xDrone_Main xdrone_main;




    private List<xDrone_Drone> xdrone_drones;


    public xDrone_Environment(
    ) {
        this.xdrone_objects = new ArrayList<>();
        this.xdrone_wallss = new ArrayList<>();
        this.xdrone_drones = new ArrayList<>();
    }

    public xDrone_Environment(
        ArrayList<xDrone_Object> xdrone_objects,        ArrayList<xDrone_Walls> xdrone_wallss,        ArrayList<xDrone_Drone> xdrone_drones    ) {
        this.xdrone_objects = xdrone_objects;
        this.xdrone_wallss = xdrone_wallss;
        this.xdrone_drones = xdrone_drones;
    }


    public List<xDrone_Object> getXdrone_objects() {
        return xdrone_objects;
    }

    public void addXdrone_object(Xdrone_object xdrone_object) {
        this.xdrone_objects.add(xdrone_object);
    }
    public List<xDrone_Walls> getXdrone_wallss() {
        return xdrone_wallss;
    }

    public void addXdrone_walls(Xdrone_walls xdrone_walls) {
        this.xdrone_wallss.add(xdrone_walls);
    }
    public xDrone_Main getXdrone_main() {
        return xdrone_main;
    }

    public void setXdrone_main(xDrone_Main xdrone_main) {
        this.xdrone_main = xdrone_main;
    }
    public List<xDrone_Drone> getXdrone_drones() {
        return xdrone_drones;
    }

    public void addXdrone_drone(Xdrone_drone xdrone_drone) {
        this.xdrone_drones.add(xdrone_drone);
    }

}