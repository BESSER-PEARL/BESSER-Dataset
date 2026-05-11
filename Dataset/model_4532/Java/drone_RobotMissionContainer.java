





import java.util.List;
import java.util.ArrayList;

public class drone_RobotMissionContainer  {






    private List<drone_Mission> drone_missions;




    private List<drone_Robot> drone_robots;




    private drone_PropertyKeyContainer drone_propertykeycontainer;




    private List<drone_AreaObject> drone_areaobjects;




    private List<drone_Capability> drone_capabilitys;




    private List<drone_MeasureDimension> drone_measuredimensions;


    public drone_RobotMissionContainer(
    ) {
        this.drone_missions = new ArrayList<>();
        this.drone_robots = new ArrayList<>();
        this.drone_areaobjects = new ArrayList<>();
        this.drone_capabilitys = new ArrayList<>();
        this.drone_measuredimensions = new ArrayList<>();
    }

    public drone_RobotMissionContainer(
        ArrayList<drone_Mission> drone_missions,        ArrayList<drone_Robot> drone_robots,        ArrayList<drone_AreaObject> drone_areaobjects,        ArrayList<drone_Capability> drone_capabilitys,        ArrayList<drone_MeasureDimension> drone_measuredimensions    ) {
        this.drone_missions = drone_missions;
        this.drone_robots = drone_robots;
        this.drone_areaobjects = drone_areaobjects;
        this.drone_capabilitys = drone_capabilitys;
        this.drone_measuredimensions = drone_measuredimensions;
    }


    public List<drone_Mission> getDrone_missions() {
        return drone_missions;
    }

    public void addDrone_mission(Drone_mission drone_mission) {
        this.drone_missions.add(drone_mission);
    }
    public List<drone_Robot> getDrone_robots() {
        return drone_robots;
    }

    public void addDrone_robot(Drone_robot drone_robot) {
        this.drone_robots.add(drone_robot);
    }
    public drone_PropertyKeyContainer getDrone_propertykeycontainer() {
        return drone_propertykeycontainer;
    }

    public void setDrone_propertykeycontainer(drone_PropertyKeyContainer drone_propertykeycontainer) {
        this.drone_propertykeycontainer = drone_propertykeycontainer;
    }
    public List<drone_AreaObject> getDrone_areaobjects() {
        return drone_areaobjects;
    }

    public void addDrone_areaobject(Drone_areaobject drone_areaobject) {
        this.drone_areaobjects.add(drone_areaobject);
    }
    public List<drone_Capability> getDrone_capabilitys() {
        return drone_capabilitys;
    }

    public void addDrone_capability(Drone_capability drone_capability) {
        this.drone_capabilitys.add(drone_capability);
    }
    public List<drone_MeasureDimension> getDrone_measuredimensions() {
        return drone_measuredimensions;
    }

    public void addDrone_measuredimension(Drone_measuredimension drone_measuredimension) {
        this.drone_measuredimensions.add(drone_measuredimension);
    }

}