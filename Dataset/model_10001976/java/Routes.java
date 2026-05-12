





import java.util.List;
import java.util.ArrayList;

public class Routes  {

    private String RouteID;
    private String DestinationAirport;
    private String OriginAirport;





    private List<Flight> flights;


    public Routes(
        String RouteID,        String DestinationAirport,        String OriginAirport    ) {
        this.RouteID = RouteID;
        this.DestinationAirport = DestinationAirport;
        this.OriginAirport = OriginAirport;
        this.flights = new ArrayList<>();
    }

    public Routes(
        String RouteID,        String DestinationAirport,        String OriginAirport        ArrayList<Flight> flights    ) {
        this.RouteID = RouteID;
        this.DestinationAirport = DestinationAirport;
        this.OriginAirport = OriginAirport;
        this.flights = flights;
    }

    public String getRouteid() {
        return RouteID;
    }

    public void setRouteid(String RouteID) {
        this.RouteID = RouteID;
    }
    public String getDestinationairport() {
        return DestinationAirport;
    }

    public void setDestinationairport(String DestinationAirport) {
        this.DestinationAirport = DestinationAirport;
    }
    public String getOriginairport() {
        return OriginAirport;
    }

    public void setOriginairport(String OriginAirport) {
        this.OriginAirport = OriginAirport;
    }

    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }

}