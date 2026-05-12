





import java.util.List;
import java.util.ArrayList;

public class Seats  {

    private String Seat_NO;
    private String Seat_Catoegry;
    private String Seat_ID;





    private Passengers passengers;


    public Seats(
        String Seat_NO,        String Seat_Catoegry,        String Seat_ID    ) {
        this.Seat_NO = Seat_NO;
        this.Seat_Catoegry = Seat_Catoegry;
        this.Seat_ID = Seat_ID;
    }


    public String getSeat_no() {
        return Seat_NO;
    }

    public void setSeat_no(String Seat_NO) {
        this.Seat_NO = Seat_NO;
    }
    public String getSeat_catoegry() {
        return Seat_Catoegry;
    }

    public void setSeat_catoegry(String Seat_Catoegry) {
        this.Seat_Catoegry = Seat_Catoegry;
    }
    public String getSeat_id() {
        return Seat_ID;
    }

    public void setSeat_id(String Seat_ID) {
        this.Seat_ID = Seat_ID;
    }

    public Passengers getPassengers() {
        return passengers;
    }

    public void setPassengers(Passengers passengers) {
        this.passengers = passengers;
    }

}