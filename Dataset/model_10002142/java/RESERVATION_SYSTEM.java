





import java.util.List;
import java.util.ArrayList;

public class RESERVATION_SYSTEM  {

    private int Reservation_ID;
    private int Reservation_Date;





    private FLIGHT flight;


    public RESERVATION_SYSTEM(
        int Reservation_ID,        int Reservation_Date    ) {
        this.Reservation_ID = Reservation_ID;
        this.Reservation_Date = Reservation_Date;
    }


    public int getReservation_id() {
        return Reservation_ID;
    }

    public void setReservation_id(int Reservation_ID) {
        this.Reservation_ID = Reservation_ID;
    }
    public int getReservation_date() {
        return Reservation_Date;
    }

    public void setReservation_date(int Reservation_Date) {
        this.Reservation_Date = Reservation_Date;
    }

    public FLIGHT getFlight() {
        return flight;
    }

    public void setFlight(FLIGHT flight) {
        this.flight = flight;
    }

}