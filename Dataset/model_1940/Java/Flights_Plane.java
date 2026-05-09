





import java.util.List;
import java.util.ArrayList;

public class Flights_Plane extends FlightObject {

    private int capacity;





    private Flights_Flight flights_flight;




    private Flights_Planes flights_planes;




    private List<Flights_Flight> flights_flights;


    public Flights_Plane(
        int capacity    ) {
        super(
        );
        this.capacity = capacity;
        this.flights_flights = new ArrayList<>();
    }

    public Flights_Plane(
        int capacity        ArrayList<Flights_Flight> flights_flights    ) {
        this.capacity = capacity;
        this.flights_flights = flights_flights;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public Flights_Flight getFlights_flight() {
        return flights_flight;
    }

    public void setFlights_flight(Flights_Flight flights_flight) {
        this.flights_flight = flights_flight;
    }
    public Flights_Planes getFlights_planes() {
        return flights_planes;
    }

    public void setFlights_planes(Flights_Planes flights_planes) {
        this.flights_planes = flights_planes;
    }
    public List<Flights_Flight> getFlights_flights() {
        return flights_flights;
    }

    public void addFlights_flight(Flights_flight flights_flight) {
        this.flights_flights.add(flights_flight);
    }

}