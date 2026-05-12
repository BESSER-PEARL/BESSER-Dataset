




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private int booking_id;
    private LocalDate date;
    private String reservedTables;
    private String customer_name;
    private String email_id;
    private String startTime;
    private int contact_no;
    private String endTime;





    private ReservationManagementSystem reservationmanagementsystem;


    public Booking(
        int booking_id,        LocalDate date,        String reservedTables,        String customer_name,        String email_id,        String startTime,        int contact_no,        String endTime    ) {
        this.booking_id = booking_id;
        this.date = date;
        this.reservedTables = reservedTables;
        this.customer_name = customer_name;
        this.email_id = email_id;
        this.startTime = startTime;
        this.contact_no = contact_no;
        this.endTime = endTime;
    }


    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
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
    public String getCustomer_name() {
        return customer_name;
    }

    public void setCustomer_name(String customer_name) {
        this.customer_name = customer_name;
    }
    public String getEmail_id() {
        return email_id;
    }

    public void setEmail_id(String email_id) {
        this.email_id = email_id;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}