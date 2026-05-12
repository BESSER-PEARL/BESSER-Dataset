





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int Number;
    private int Guests;





    private List<Reservation> reservations;


    public Room(
        int Number,        int Guests    ) {
        this.Number = Number;
        this.Guests = Guests;
        this.reservations = new ArrayList<>();
    }

    public Room(
        int Number,        int Guests        ArrayList<Reservation> reservations    ) {
        this.Number = Number;
        this.Guests = Guests;
        this.reservations = reservations;
    }

    public int getNumber() {
        return Number;
    }

    public void setNumber(int Number) {
        this.Number = Number;
    }
    public int getGuests() {
        return Guests;
    }

    public void setGuests(int Guests) {
        this.Guests = Guests;
    }

    public List<Reservation> getReservations() {
        return reservations;
    }

    public void addReservation(Reservation reservation) {
        this.reservations.add(reservation);
    }

}