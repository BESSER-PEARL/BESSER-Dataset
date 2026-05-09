





import java.util.List;
import java.util.ArrayList;

public class Flights_Route extends FlightObject {

    private int duration;





    private List<Flights_Flight> flights_flights;




    private Flights_Routes flights_routes;




    private Flights_Flight flights_flight;


    public Flights_Route(
        int duration    ) {
        super(
        );
        this.duration = duration;
        this.flights_flights = new ArrayList<>();
    }

    public Flights_Route(
        int duration        ArrayList<Flights_Flight> flights_flights    ) {
        this.duration = duration;
        this.flights_flights = flights_flights;
    }

    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }

    public List<Flights_Flight> getFlights_flights() {
        return flights_flights;
    }

    public void addFlights_flight(Flights_flight flights_flight) {
        this.flights_flights.add(flights_flight);
    }
    public Flights_Routes getFlights_routes() {
        return flights_routes;
    }

    public void setFlights_routes(Flights_Routes flights_routes) {
        this.flights_routes = flights_routes;
    }
    public Flights_Flight getFlights_flight() {
        return flights_flight;
    }

    public void setFlights_flight(Flights_Flight flights_flight) {
        this.flights_flight = flights_flight;
    }

}