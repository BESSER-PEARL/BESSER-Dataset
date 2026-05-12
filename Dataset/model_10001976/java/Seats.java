





import java.util.List;
import java.util.ArrayList;

public class Seats  {

    private int SeatNumber;
    private boolean Availability;





    private List<Plane> planes;


    public Seats(
        int SeatNumber,        boolean Availability    ) {
        this.SeatNumber = SeatNumber;
        this.Availability = Availability;
        this.planes = new ArrayList<>();
    }

    public Seats(
        int SeatNumber,        boolean Availability        ArrayList<Plane> planes    ) {
        this.SeatNumber = SeatNumber;
        this.Availability = Availability;
        this.planes = planes;
    }

    public int getSeatnumber() {
        return SeatNumber;
    }

    public void setSeatnumber(int SeatNumber) {
        this.SeatNumber = SeatNumber;
    }
    public boolean getAvailability() {
        return Availability;
    }

    public void setAvailability(boolean Availability) {
        this.Availability = Availability;
    }

    public List<Plane> getPlanes() {
        return planes;
    }

    public void addPlane(Plane plane) {
        this.planes.add(plane);
    }

}