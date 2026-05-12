





import java.util.List;
import java.util.ArrayList;

public class Airport  {

    private String location;
    private int code;
    private String name;





    private List<Flight> flights;


    public Airport(
        String location,        int code,        String name    ) {
        this.location = location;
        this.code = code;
        this.name = name;
        this.flights = new ArrayList<>();
    }

    public Airport(
        String location,        int code,        String name        ArrayList<Flight> flights    ) {
        this.location = location;
        this.code = code;
        this.name = name;
        this.flights = flights;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}