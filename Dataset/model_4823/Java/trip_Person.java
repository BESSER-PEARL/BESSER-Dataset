





import java.util.List;
import java.util.ArrayList;

public class trip_Person extends NamedElement {






    private List<trip_Trip> trip_trips;




    private trip_Trip trip_trip;




    private trip_Trip trip_trip;


    public trip_Person(
    ) {
        super(
        );
        this.trip_trips = new ArrayList<>();
    }

    public trip_Person(
        ArrayList<trip_Trip> trip_trips    ) {
        this.trip_trips = trip_trips;
    }


    public List<trip_Trip> getTrip_trips() {
        return trip_trips;
    }

    public void addTrip_trip(Trip_trip trip_trip) {
        this.trip_trips.add(trip_trip);
    }
    public trip_Trip getTrip_trip() {
        return trip_trip;
    }

    public void setTrip_trip(trip_Trip trip_trip) {
        this.trip_trip = trip_trip;
    }
    public trip_Trip getTrip_trip() {
        return trip_trip;
    }

    public void setTrip_trip(trip_Trip trip_trip) {
        this.trip_trip = trip_trip;
    }

}