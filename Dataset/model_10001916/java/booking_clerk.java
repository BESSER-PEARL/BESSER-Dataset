





import java.util.List;
import java.util.ArrayList;

public class booking_clerk  {






    private List<Passenger> passengers;


    public booking_clerk(
    ) {
        this.passengers = new ArrayList<>();
    }

    public booking_clerk(
        ArrayList<Passenger> passengers    ) {
        this.passengers = passengers;
    }


    public List<Passenger> getPassengers() {
        return passengers;
    }

    public void addPassenger(Passenger passenger) {
        this.passengers.add(passenger);
    }

}