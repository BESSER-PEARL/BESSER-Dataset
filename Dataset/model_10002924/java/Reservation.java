





import java.util.List;
import java.util.ArrayList;

public class Reservation  {

    private String End;
    private String Start;
    private int Reservation_id;





    private List<Guest> guests;


    public Reservation(
        String End,        String Start,        int Reservation_id    ) {
        this.End = End;
        this.Start = Start;
        this.Reservation_id = Reservation_id;
        this.guests = new ArrayList<>();
    }

    public Reservation(
        String End,        String Start,        int Reservation_id        ArrayList<Guest> guests    ) {
        this.End = End;
        this.Start = Start;
        this.Reservation_id = Reservation_id;
        this.guests = guests;
    }

    public String getEnd() {
        return End;
    }

    public void setEnd(String End) {
        this.End = End;
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

    public List<Guest> getGuests() {
        return guests;
    }

    public void addGuest(Guest guest) {
        this.guests.add(guest);
    }

}