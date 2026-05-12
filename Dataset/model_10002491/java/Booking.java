




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private int contact_no;
    private LocalDate date;
    private String startTime;
    private int b_id;
    private String email_id;
    private String endTime;
    private String reservedTables;
    private String customer_name;





    private ReservationManagementSystem reservationmanagementsystem;


    public Booking(
        int contact_no,        LocalDate date,        String startTime,        int b_id,        String email_id,        String endTime,        String reservedTables,        String customer_name    ) {
        this.contact_no = contact_no;
        this.date = date;
        this.startTime = startTime;
        this.b_id = b_id;
        this.email_id = email_id;
        this.endTime = endTime;
        this.reservedTables = reservedTables;
        this.customer_name = customer_name;
    }


    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public int getB_id() {
        return b_id;
    }

    public void setB_id(int b_id) {
        this.b_id = b_id;
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

    public ReservationManagementSystem getReservationmanagementsystem() {
        return reservationmanagementsystem;
    }

    public void setReservationmanagementsystem(ReservationManagementSystem reservationmanagementsystem) {
        this.reservationmanagementsystem = reservationmanagementsystem;
    }

}