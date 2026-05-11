





import java.util.List;
import java.util.ArrayList;

public class platoon_Platoon  {

    private int length;
    private int desiredGapSize;





    private platoon_Platoon platoon_platoon;




    private List<platoon_PlatoonVehicle> platoon_platoonvehicles;




    private platoon_PlatoonVehicle platoon_platoonvehicle;




    private platoon_PlatoonVehicle platoon_platoonvehicle;




    private List<platoon_PlatoonVehicle> platoon_platoonvehicles;


    public platoon_Platoon(
        int length,        int desiredGapSize    ) {
        this.length = length;
        this.desiredGapSize = desiredGapSize;
        this.platoon_platoonvehicles = new ArrayList<>();
        this.platoon_platoonvehicles = new ArrayList<>();
    }

    public platoon_Platoon(
        int length,        int desiredGapSize        ArrayList<platoon_PlatoonVehicle> platoon_platoonvehicles,        ArrayList<platoon_PlatoonVehicle> platoon_platoonvehicles    ) {
        this.length = length;
        this.desiredGapSize = desiredGapSize;
        this.platoon_platoonvehicles = platoon_platoonvehicles;
        this.platoon_platoonvehicles = platoon_platoonvehicles;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getDesiredgapsize() {
        return desiredGapSize;
    }

    public void setDesiredgapsize(int desiredGapSize) {
        this.desiredGapSize = desiredGapSize;
    }

    public platoon_Platoon getPlatoon_platoon() {
        return platoon_platoon;
    }

    public void setPlatoon_platoon(platoon_Platoon platoon_platoon) {
        this.platoon_platoon = platoon_platoon;
    }
    public List<platoon_PlatoonVehicle> getPlatoon_platoonvehicles() {
        return platoon_platoonvehicles;
    }

    public void addPlatoon_platoonvehicle(Platoon_platoonvehicle platoon_platoonvehicle) {
        this.platoon_platoonvehicles.add(platoon_platoonvehicle);
    }
    public platoon_PlatoonVehicle getPlatoon_platoonvehicle() {
        return platoon_platoonvehicle;
    }

    public void setPlatoon_platoonvehicle(platoon_PlatoonVehicle platoon_platoonvehicle) {
        this.platoon_platoonvehicle = platoon_platoonvehicle;
    }
    public platoon_PlatoonVehicle getPlatoon_platoonvehicle() {
        return platoon_platoonvehicle;
    }

    public void setPlatoon_platoonvehicle(platoon_PlatoonVehicle platoon_platoonvehicle) {
        this.platoon_platoonvehicle = platoon_platoonvehicle;
    }
    public List<platoon_PlatoonVehicle> getPlatoon_platoonvehicles() {
        return platoon_platoonvehicles;
    }

    public void addPlatoon_platoonvehicle(Platoon_platoonvehicle platoon_platoonvehicle) {
        this.platoon_platoonvehicles.add(platoon_platoonvehicle);
    }

}