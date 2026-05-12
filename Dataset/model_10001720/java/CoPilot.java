





import java.util.List;
import java.util.ArrayList;

public class CoPilot  {






    private List<Aircraft> aircrafts;


    public CoPilot(
    ) {
        this.aircrafts = new ArrayList<>();
    }

    public CoPilot(
        ArrayList<Aircraft> aircrafts    ) {
        this.aircrafts = aircrafts;
    }


    public List<Aircraft> getAircrafts() {
        return aircrafts;
    }

    public void addAircraft(Aircraft aircraft) {
        this.aircrafts.add(aircraft);
    }

}