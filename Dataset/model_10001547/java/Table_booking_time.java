





import java.util.List;
import java.util.ArrayList;

public class Table_booking_time  {

    private int end_time;
    private int start_time;





    private Booking booking;




    private Payment payment;


    public Table_booking_time(
        int end_time,        int start_time    ) {
        this.end_time = end_time;
        this.start_time = start_time;
    }


    public int getEnd_time() {
        return end_time;
    }

    public void setEnd_time(int end_time) {
        this.end_time = end_time;
    }
    public int getStart_time() {
        return start_time;
    }

    public void setStart_time(int start_time) {
        this.start_time = start_time;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}