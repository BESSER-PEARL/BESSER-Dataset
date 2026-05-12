





import java.util.List;
import java.util.ArrayList;

public class Restaurant  {

    private int booking;
    private int time;



    public Restaurant(
        int booking,        int time    ) {
        this.booking = booking;
        this.time = time;
    }


    public int getBooking() {
        return booking;
    }

    public void setBooking(int booking) {
        this.booking = booking;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }


}