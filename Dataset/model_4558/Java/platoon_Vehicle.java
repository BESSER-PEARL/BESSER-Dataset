





import java.util.List;
import java.util.ArrayList;

public class platoon_Vehicle  {

    private String name;





    private platoon_FollowingVehicle platoon_followingvehicle;


    public platoon_Vehicle(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public platoon_FollowingVehicle getPlatoon_followingvehicle() {
        return platoon_followingvehicle;
    }

    public void setPlatoon_followingvehicle(platoon_FollowingVehicle platoon_followingvehicle) {
        this.platoon_followingvehicle = platoon_followingvehicle;
    }

}