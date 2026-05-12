




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String customer_name;
    private LocalDate date;
    private int booking_id;
    private String email_id;
    private String endTime;
    private int contact_no;
    private String reservedTables;
    private String startTime;





    private ReservationManagementSystem reservationmanagementsystem;


    public Booking(
        String customer_name,        LocalDate date,        int booking_id,        String email_id,        String endTime,        int contact_no,        String reservedTables,        String startTime    ) {
        this.customer_name = customer_name;
        this.date = date;
        this.booking_id = booking_id;
        this.email_id = email_id;
        this.endTime = endTime;
        this.contact_no = contact_no;
        this.reservedTables = reservedTables;
        this.startTime = startTime;
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
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
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
    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
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

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}