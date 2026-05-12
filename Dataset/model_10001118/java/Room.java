





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int Guests;
    private int Number;





    private List<Reservation> reservations;


    public Room(
        int Guests,        int Number    ) {
        this.Guests = Guests;
        this.Number = Number;
        this.reservations = new ArrayList<>();
    }

    public Room(
        int Guests,        int Number        ArrayList<Reservation> reservations    ) {
        this.Guests = Guests;
        this.Number = Number;
        this.reservations = reservations;
    }

    public int getGuests() {
        return Guests;
    }

    public void setGuests(int Guests) {
        this.Guests = Guests;
    }
    public int getNumber() {
        return Number;
    }

    public void setNumber(int Number) {
        this.Number = Number;
    }

    public List<Reservation> getReservations() {
        return reservations;
    }

    public void addReservation(Reservation reservation) {
        this.reservations.add(reservation);
    }

}