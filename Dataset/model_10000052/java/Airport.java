





import java.util.List;
import java.util.ArrayList;

public class Airport  {

    private String id;





    private List<Flight> flights;




    private List<Flight> flights;


    public Airport(
        String id    ) {
        this.id = id;
        this.flights = new ArrayList<>();
        this.flights = new ArrayList<>();
    }

    public Airport(
        String id        ArrayList<Flight> flights,        ArrayList<Flight> flights    ) {
        this.id = id;
        this.flights = flights;
        this.flights = flights;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }
    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}