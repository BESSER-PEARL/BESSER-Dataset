





import java.util.List;
import java.util.ArrayList;

public class platoon_Platoon  {






    private platoon_LeaderVehicle platoon_leadervehicle;




    private platoon_Root platoon_root;




    private List<platoon_FollowingVehicle> platoon_followingvehicles;


    public platoon_Platoon(
    ) {
        this.platoon_followingvehicles = new ArrayList<>();
    }

    public platoon_Platoon(
        ArrayList<platoon_FollowingVehicle> platoon_followingvehicles    ) {
        this.platoon_followingvehicles = platoon_followingvehicles;
    }


    public platoon_LeaderVehicle getPlatoon_leadervehicle() {
        return platoon_leadervehicle;
    }

    public void setPlatoon_leadervehicle(platoon_LeaderVehicle platoon_leadervehicle) {
        this.platoon_leadervehicle = platoon_leadervehicle;
    }
    public platoon_Root getPlatoon_root() {
        return platoon_root;
    }

    public void setPlatoon_root(platoon_Root platoon_root) {
        this.platoon_root = platoon_root;
    }
    public List<platoon_FollowingVehicle> getPlatoon_followingvehicles() {
        return platoon_followingvehicles;
    }

    public void addPlatoon_followingvehicle(Platoon_followingvehicle platoon_followingvehicle) {
        this.platoon_followingvehicles.add(platoon_followingvehicle);
    }

}