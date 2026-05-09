





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Seat  {

    private String no;
    private boolean isExit;
    private int type;





    private reservationsystem_Booking reservationsystem_booking;




    private reservationsystem_Booking reservationsystem_booking;


    public reservationsystem_Seat(
        String no,        boolean isExit,        int type    ) {
        this.no = no;
        this.isExit = isExit;
        this.type = type;
    }


    public String getNo() {
        return no;
    }

    public void setNo(String no) {
        this.no = no;
    }
    public boolean getIsexit() {
        return isExit;
    }

    public void setIsexit(boolean isExit) {
        this.isExit = isExit;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public reservationsystem_Booking getReservationsystem_booking() {
        return reservationsystem_booking;
    }

    public void setReservationsystem_booking(reservationsystem_Booking reservationsystem_booking) {
        this.reservationsystem_booking = reservationsystem_booking;
    }
    public reservationsystem_Booking getReservationsystem_booking() {
        return reservationsystem_booking;
    }

    public void setReservationsystem_booking(reservationsystem_Booking reservationsystem_booking) {
        this.reservationsystem_booking = reservationsystem_booking;
    }

}