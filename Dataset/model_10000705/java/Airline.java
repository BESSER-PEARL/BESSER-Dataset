





import java.util.List;
import java.util.ArrayList;

public class Airline  {

    private String id;





    private List<Aircraft> aircrafts;




    private List<Flight> flights;


    public Airline(
        String id    ) {
        this.id = id;
        this.aircrafts = new ArrayList<>();
        this.flights = new ArrayList<>();
    }

    public Airline(
        String id        ArrayList<Aircraft> aircrafts,        ArrayList<Flight> flights    ) {
        this.id = id;
        this.aircrafts = aircrafts;
        this.flights = flights;
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
    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}