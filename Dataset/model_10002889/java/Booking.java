




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String startTime;
    private String email_id;
    private String endTime;
    private String customer_name;
    private LocalDate date;
    private String reservedTables;
    private int contact_no;
    private int booking_id;





    private ReservationManagementSystem reservationmanagementsystem;


    public Booking(
        String startTime,        String email_id,        String endTime,        String customer_name,        LocalDate date,        String reservedTables,        int contact_no,        int booking_id    ) {
        this.startTime = startTime;
        this.email_id = email_id;
        this.endTime = endTime;
        this.customer_name = customer_name;
        this.date = date;
        this.reservedTables = reservedTables;
        this.contact_no = contact_no;
        this.booking_id = booking_id;
    }


    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public String getEmail_id() {
        return email_id;
    }

    public void setEmail_id(String email_id) {
        this.email_id = email_id;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }
    public String getCustomer_name() {
        return customer_name;
    }

    public void setCustomer_name(String customer_name) {
        this.customer_name = customer_name;
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
    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}