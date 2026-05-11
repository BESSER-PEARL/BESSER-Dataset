





import java.util.List;
import java.util.ArrayList;

public class platoon_FrontGap  {

    private int actualGapSize;





    private platoon_JoiningVehicle platoon_joiningvehicle;




    private platoon_PlatoonVehicle platoon_platoonvehicle;


    public platoon_FrontGap(
        int actualGapSize    ) {
        this.actualGapSize = actualGapSize;
    }


    public int getActualgapsize() {
        return actualGapSize;
    }

    public void setActualgapsize(int actualGapSize) {
        this.actualGapSize = actualGapSize;
    }

    public platoon_JoiningVehicle getPlatoon_joiningvehicle() {
        return platoon_joiningvehicle;
    }

    public void setPlatoon_joiningvehicle(platoon_JoiningVehicle platoon_joiningvehicle) {
        this.platoon_joiningvehicle = platoon_joiningvehicle;
    }
    public platoon_PlatoonVehicle getPlatoon_platoonvehicle() {
        return platoon_platoonvehicle;
    }

    public void setPlatoon_platoonvehicle(platoon_PlatoonVehicle platoon_platoonvehicle) {
        this.platoon_platoonvehicle = platoon_platoonvehicle;
    }

}