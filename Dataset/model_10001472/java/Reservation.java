





import java.util.List;
import java.util.ArrayList;

public class Reservation  {

    private String Start;
    private int Reservation_id;
    private String End;





    private List<Guest> guests;


    public Reservation(
        String Start,        int Reservation_id,        String End    ) {
        this.Start = Start;
        this.Reservation_id = Reservation_id;
        this.End = End;
        this.guests = new ArrayList<>();
    }

    public Reservation(
        String Start,        int Reservation_id,        String End        ArrayList<Guest> guests    ) {
        this.Start = Start;
        this.Reservation_id = Reservation_id;
        this.End = End;
        this.guests = guests;
    }

    public String getStart() {
        return Start;
    }

    public void setStart(String Start) {
        this.Start = Start;
    }
    public int getReservation_id() {
        return Reservation_id;
    }

    public void setReservation_id(int Reservation_id) {
        this.Reservation_id = Reservation_id;
    }
    public String getEnd() {
        return End;
    }

    public void setEnd(String End) {
        this.End = End;
    }

    public List<Guest> getGuests() {
        return guests;
    }

    public void addGuest(Guest guest) {
        this.guests.add(guest);
    }

}