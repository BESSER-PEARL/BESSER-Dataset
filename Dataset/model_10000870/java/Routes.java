





import java.util.List;
import java.util.ArrayList;

public class Routes  {

    private String OriginAirport;
    private String DestinationAirport;
    private String RouteID;





    private List<Flight> flights;


    public Routes(
        String OriginAirport,        String DestinationAirport,        String RouteID    ) {
        this.OriginAirport = OriginAirport;
        this.DestinationAirport = DestinationAirport;
        this.RouteID = RouteID;
        this.flights = new ArrayList<>();
    }

    public Routes(
        String OriginAirport,        String DestinationAirport,        String RouteID        ArrayList<Flight> flights    ) {
        this.OriginAirport = OriginAirport;
        this.DestinationAirport = DestinationAirport;
        this.RouteID = RouteID;
        this.flights = flights;
    }

    public String getOriginairport() {
        return OriginAirport;
    }

    public void setOriginairport(String OriginAirport) {
        this.OriginAirport = OriginAirport;
    }
    public String getDestinationairport() {
        return DestinationAirport;
    }

    public void setDestinationairport(String DestinationAirport) {
        this.DestinationAirport = DestinationAirport;
    }
    public String getRouteid() {
        return RouteID;
    }

    public void setRouteid(String RouteID) {
        this.RouteID = RouteID;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}