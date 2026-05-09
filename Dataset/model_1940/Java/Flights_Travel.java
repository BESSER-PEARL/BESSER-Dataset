





import java.util.List;
import java.util.ArrayList;

public class Flights_Travel extends FlightObject {






    private Flights_Person flights_person;




    private List<Flights_Flight> flights_flights;




    private Flights_Person flights_person;




    private Flights_Flight flights_flight;


    public Flights_Travel(
    ) {
        super(
        );
        this.flights_flights = new ArrayList<>();
    }

    public Flights_Travel(
        ArrayList<Flights_Flight> flights_flights    ) {
        this.flights_flights = flights_flights;
    }


    public Flights_Person getFlights_person() {
        return flights_person;
    }

    public void setFlights_person(Flights_Person flights_person) {
        this.flights_person = flights_person;
    }
    public List<Flights_Flight> getFlights_flights() {
        return flights_flights;
    }

    public void addFlights_flight(Flights_flight flights_flight) {
        this.flights_flights.add(flights_flight);
    }
    public Flights_Person getFlights_person() {
        return flights_person;
    }

    public void setFlights_person(Flights_Person flights_person) {
        this.flights_person = flights_person;
    }
    public Flights_Flight getFlights_flight() {
        return flights_flight;
    }

    public void setFlights_flight(Flights_Flight flights_flight) {
        this.flights_flight = flights_flight;
    }

}