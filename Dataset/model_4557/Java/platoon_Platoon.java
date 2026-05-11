





import java.util.List;
import java.util.ArrayList;

public class platoon_Platoon  {






    private platoon_World platoon_world;




    private List<platoon_FollowVehicle> platoon_followvehicles;




    private platoon_LeadVehicle platoon_leadvehicle;


    public platoon_Platoon(
    ) {
        this.platoon_followvehicles = new ArrayList<>();
    }

    public platoon_Platoon(
        ArrayList<platoon_FollowVehicle> platoon_followvehicles    ) {
        this.platoon_followvehicles = platoon_followvehicles;
    }


    public platoon_World getPlatoon_world() {
        return platoon_world;
    }

    public void setPlatoon_world(platoon_World platoon_world) {
        this.platoon_world = platoon_world;
    }
    public List<platoon_FollowVehicle> getPlatoon_followvehicles() {
        return platoon_followvehicles;
    }

    public void addPlatoon_followvehicle(Platoon_followvehicle platoon_followvehicle) {
        this.platoon_followvehicles.add(platoon_followvehicle);
    }
    public platoon_LeadVehicle getPlatoon_leadvehicle() {
        return platoon_leadvehicle;
    }

    public void setPlatoon_leadvehicle(platoon_LeadVehicle platoon_leadvehicle) {
        this.platoon_leadvehicle = platoon_leadvehicle;
    }

}