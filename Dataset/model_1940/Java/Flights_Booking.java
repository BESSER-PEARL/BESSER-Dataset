





import java.util.List;
import java.util.ArrayList;

public class Flights_Booking extends FlightObject {






    private Flights_Bookings flights_bookings;




    private List<Flights_Travel> flights_travels;


    public Flights_Booking(
    ) {
        super(
        );
        this.flights_travels = new ArrayList<>();
    }

    public Flights_Booking(
        ArrayList<Flights_Travel> flights_travels    ) {
        this.flights_travels = flights_travels;
    }


    public Flights_Bookings getFlights_bookings() {
        return flights_bookings;
    }

    public void setFlights_bookings(Flights_Bookings flights_bookings) {
        this.flights_bookings = flights_bookings;
    }
    public List<Flights_Travel> getFlights_travels() {
        return flights_travels;
    }

    public void addFlights_travel(Flights_travel flights_travel) {
        this.flights_travels.add(flights_travel);
    }

}