





import java.util.List;
import java.util.ArrayList;

public class trip_Vehicle extends NamedElement {

    private int nrOfSeats;





    private trip_Trip trip_trip;


    public trip_Vehicle(
        int nrOfSeats    ) {
        super(
        );
        this.nrOfSeats = nrOfSeats;
    }


    public int getNrofseats() {
        return nrOfSeats;
    }

    public void setNrofseats(int nrOfSeats) {
        this.nrOfSeats = nrOfSeats;
    }

    public trip_Trip getTrip_trip() {
        return trip_trip;
    }

    public void setTrip_trip(trip_Trip trip_trip) {
        this.trip_trip = trip_trip;
    }

}