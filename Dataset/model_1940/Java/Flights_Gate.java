





import java.util.List;
import java.util.ArrayList;

public class Flights_Gate extends FlightObject {

    private int position;





    private Flights_Flight flights_flight;




    private Flights_Flight flights_flight;




    private List<Flights_Flight> flights_flights;




    private List<Flights_Flight> flights_flights;


    public Flights_Gate(
        int position    ) {
        super(
        );
        this.position = position;
        this.flights_flights = new ArrayList<>();
        this.flights_flights = new ArrayList<>();
    }

    public Flights_Gate(
        int position        ArrayList<Flights_Flight> flights_flights,        ArrayList<Flights_Flight> flights_flights    ) {
        this.position = position;
        this.flights_flights = flights_flights;
        this.flights_flights = flights_flights;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }

    public Flights_Flight getFlights_flight() {
        return flights_flight;
    }

    public void setFlights_flight(Flights_Flight flights_flight) {
        this.flights_flight = flights_flight;
    }
    public Flights_Flight getFlights_flight() {
        return flights_flight;
    }

    public void setFlights_flight(Flights_Flight flights_flight) {
        this.flights_flight = flights_flight;
    }
    public List<Flights_Flight> getFlights_flights() {
        return flights_flights;
    }

    public void addFlights_flight(Flights_flight flights_flight) {
        this.flights_flights.add(flights_flight);
    }
    public List<Flights_Flight> getFlights_flights() {
        return flights_flights;
    }

    public void addFlights_flight(Flights_flight flights_flight) {
        this.flights_flights.add(flights_flight);
    }

}