





import java.util.List;
import java.util.ArrayList;

public class DistributionSystem_Customer  {

    private int _milesFlyed;
    private String name;
    private String Luggage;





    private List<DistributionSystem_BoardingPass> distributionsystem_boardingpasss;


    public DistributionSystem_Customer(
        int _milesFlyed,        String name,        String Luggage    ) {
        this._milesFlyed = _milesFlyed;
        this.name = name;
        this.Luggage = Luggage;
        this.distributionsystem_boardingpasss = new ArrayList<>();
    }

    public DistributionSystem_Customer(
        int _milesFlyed,        String name,        String Luggage        ArrayList<DistributionSystem_BoardingPass> distributionsystem_boardingpasss    ) {
        this._milesFlyed = _milesFlyed;
        this.name = name;
        this.Luggage = Luggage;
        this.distributionsystem_boardingpasss = distributionsystem_boardingpasss;
    }

    public int get_milesflyed() {
        return _milesFlyed;
    }

    public void set_milesflyed(int _milesFlyed) {
        this._milesFlyed = _milesFlyed;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLuggage() {
        return Luggage;
    }

    public void setLuggage(String Luggage) {
        this.Luggage = Luggage;
    }

    public List<DistributionSystem_BoardingPass> getDistributionsystem_boardingpasss() {
        return distributionsystem_boardingpasss;
    }

    public void addDistributionsystem_boardingpass(Distributionsystem_boardingpass distributionsystem_boardingpass) {
        this.distributionsystem_boardingpasss.add(distributionsystem_boardingpass);
    }

}