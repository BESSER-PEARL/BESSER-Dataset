





import java.util.List;
import java.util.ArrayList;

public class mission_Swarm  {






    private mission_Mission mission_mission;




    private List<mission_Drone> mission_drones;


    public mission_Swarm(
    ) {
        this.mission_drones = new ArrayList<>();
    }

    public mission_Swarm(
        ArrayList<mission_Drone> mission_drones    ) {
        this.mission_drones = mission_drones;
    }


    public mission_Mission getMission_mission() {
        return mission_mission;
    }

    public void setMission_mission(mission_Mission mission_mission) {
        this.mission_mission = mission_mission;
    }
    public List<mission_Drone> getMission_drones() {
        return mission_drones;
    }

    public void addMission_drone(Mission_drone mission_drone) {
        this.mission_drones.add(mission_drone);
    }

}