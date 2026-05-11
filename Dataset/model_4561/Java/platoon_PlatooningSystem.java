





import java.util.List;
import java.util.ArrayList;

public class platoon_PlatooningSystem  {






    private List<platoon_Platoon> platoon_platoons;




    private List<platoon_Vehicle> platoon_vehicles;


    public platoon_PlatooningSystem(
    ) {
        this.platoon_platoons = new ArrayList<>();
        this.platoon_vehicles = new ArrayList<>();
    }

    public platoon_PlatooningSystem(
        ArrayList<platoon_Platoon> platoon_platoons,        ArrayList<platoon_Vehicle> platoon_vehicles    ) {
        this.platoon_platoons = platoon_platoons;
        this.platoon_vehicles = platoon_vehicles;
    }


    public List<platoon_Platoon> getPlatoon_platoons() {
        return platoon_platoons;
    }

    public void addPlatoon_platoon(Platoon_platoon platoon_platoon) {
        this.platoon_platoons.add(platoon_platoon);
    }
    public List<platoon_Vehicle> getPlatoon_vehicles() {
        return platoon_vehicles;
    }

    public void addPlatoon_vehicle(Platoon_vehicle platoon_vehicle) {
        this.platoon_vehicles.add(platoon_vehicle);
    }

}