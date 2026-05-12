





import java.util.List;
import java.util.ArrayList;

public class Groups  {

    private None id;
    private String names;
    private None passenger_amount;





    private booking_clerk booking_clerk;




    private Passenger passenger;


    public Groups(
        None id,        String names,        None passenger_amount    ) {
        this.id = id;
        this.names = names;
        this.passenger_amount = passenger_amount;
    }


    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }
    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }
    public None getPassenger_amount() {
        return passenger_amount;
    }

    public void setPassenger_amount(None passenger_amount) {
        this.passenger_amount = passenger_amount;
    }

    public booking_clerk getBooking_clerk() {
        return booking_clerk;
    }

    public void setBooking_clerk(booking_clerk booking_clerk) {
        this.booking_clerk = booking_clerk;
    }
    public Passenger getPassenger() {
        return passenger;
    }

    public void setPassenger(Passenger passenger) {
        this.passenger = passenger;
    }

}