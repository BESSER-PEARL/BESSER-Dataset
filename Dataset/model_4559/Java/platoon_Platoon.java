





import java.util.List;
import java.util.ArrayList;

public class platoon_Platoon  {






    private List<platoon_FollowVehicle> platoon_followvehicles;




    private platoon_LeadingVehicle platoon_leadingvehicle;


    public platoon_Platoon(
    ) {
        this.platoon_followvehicles = new ArrayList<>();
    }

    public platoon_Platoon(
        ArrayList<platoon_FollowVehicle> platoon_followvehicles    ) {
        this.platoon_followvehicles = platoon_followvehicles;
    }


    public List<platoon_FollowVehicle> getPlatoon_followvehicles() {
        return platoon_followvehicles;
    }

    public void addPlatoon_followvehicle(Platoon_followvehicle platoon_followvehicle) {
        this.platoon_followvehicles.add(platoon_followvehicle);
    }
    public platoon_LeadingVehicle getPlatoon_leadingvehicle() {
        return platoon_leadingvehicle;
    }

    public void setPlatoon_leadingvehicle(platoon_LeadingVehicle platoon_leadingvehicle) {
        this.platoon_leadingvehicle = platoon_leadingvehicle;
    }

}