





import java.util.List;
import java.util.ArrayList;

public class Captain  {






    private List<Aircraft> aircrafts;


    public Captain(
    ) {
        this.aircrafts = new ArrayList<>();
    }

    public Captain(
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