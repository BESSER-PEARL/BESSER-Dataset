





import java.util.List;
import java.util.ArrayList;

public class Airline  {

    private String id;





    private List<Aircraft> aircrafts;


    public Airline(
        String id    ) {
        this.id = id;
        this.aircrafts = new ArrayList<>();
    }

    public Airline(
        String id        ArrayList<Aircraft> aircrafts    ) {
        this.id = id;
        this.aircrafts = aircrafts;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Aircraft> getAircrafts() {
        return aircrafts;
    }

    public void addAircraft(Aircraft aircraft) {
        this.aircrafts.add(aircraft);
    }

}