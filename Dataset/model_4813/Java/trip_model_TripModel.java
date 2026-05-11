





import java.util.List;
import java.util.ArrayList;

public class trip_model_TripModel  {






    private List<trip_model_Trip> trip_model_trips;




    private List<trip_model_location> trip_model_locations;


    public trip_model_TripModel(
    ) {
        this.trip_model_trips = new ArrayList<>();
        this.trip_model_locations = new ArrayList<>();
    }

    public trip_model_TripModel(
        ArrayList<trip_model_Trip> trip_model_trips,        ArrayList<trip_model_location> trip_model_locations    ) {
        this.trip_model_trips = trip_model_trips;
        this.trip_model_locations = trip_model_locations;
    }


    public List<trip_model_Trip> getTrip_model_trips() {
        return trip_model_trips;
    }

    public void addTrip_model_trip(Trip_model_trip trip_model_trip) {
        this.trip_model_trips.add(trip_model_trip);
    }
    public List<trip_model_location> getTrip_model_locations() {
        return trip_model_locations;
    }

    public void addTrip_model_location(Trip_model_location trip_model_location) {
        this.trip_model_locations.add(trip_model_location);
    }

}