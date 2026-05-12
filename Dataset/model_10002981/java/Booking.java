




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private int booking_id;
    private String reservedTables;
    private LocalDate date;
    private String endTime;
    private int contact_no;
    private String email_id;
    private String customer_name;
    private String startTime;





    private ReservationManagementSystem reservationmanagementsystem;


    public Booking(
        int booking_id,        String reservedTables,        LocalDate date,        String endTime,        int contact_no,        String email_id,        String customer_name,        String startTime    ) {
        this.booking_id = booking_id;
        this.reservedTables = reservedTables;
        this.date = date;
        this.endTime = endTime;
        this.contact_no = contact_no;
        this.email_id = email_id;
        this.customer_name = customer_name;
        this.startTime = startTime;
    }


    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
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
    public String getEmail_id() {
        return email_id;
    }

    public void setEmail_id(String email_id) {
        this.email_id = email_id;
    }
    public String getCustomer_name() {
        return customer_name;
    }

    public void setCustomer_name(String customer_name) {
        this.customer_name = customer_name;
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