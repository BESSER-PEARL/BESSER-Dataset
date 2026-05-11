





import java.util.List;
import java.util.ArrayList;

public class platoon_Vehicle  {

    private String name;





    private platoon_FollowVehicle platoon_followvehicle;


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

    public platoon_FollowVehicle getPlatoon_followvehicle() {
        return platoon_followvehicle;
    }

    public void setPlatoon_followvehicle(platoon_FollowVehicle platoon_followvehicle) {
        this.platoon_followvehicle = platoon_followvehicle;
    }

}