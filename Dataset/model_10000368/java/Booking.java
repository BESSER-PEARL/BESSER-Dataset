




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String customer_name;
    private int booking_id;
    private int contact_no;
    private String email_id;
    private LocalDate date;
    private String reservedTables;
    private String startTime;
    private String endTime;





    private Reservation_System reservation_system;


    public Booking(
        String customer_name,        int booking_id,        int contact_no,        String email_id,        LocalDate date,        String reservedTables,        String startTime,        String endTime    ) {
        this.customer_name = customer_name;
        this.booking_id = booking_id;
        this.contact_no = contact_no;
        this.email_id = email_id;
        this.date = date;
        this.reservedTables = reservedTables;
        this.startTime = startTime;
        this.endTime = endTime;
    }


    public String getCustomer_name() {
        return customer_name;
    }

    public void setCustomer_name(String customer_name) {
        this.customer_name = customer_name;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }
    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
    }
    public String getEmail_id() {
        return email_id;
    }

    public void setEmail_id(String email_id) {
        this.email_id = email_id;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }

    public Reservation_System getReservation_system() {
        return reservation_system;
    }

    public void setReservation_system(Reservation_System reservation_system) {
        this.reservation_system = reservation_system;
    }

}