




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String FirstName;
    private LocalDate LeaveDate;
    private int phoneNumber;
    private LocalDate Booking_Date;
    private String LastName;



    public Customer(
        String FirstName,        LocalDate LeaveDate,        int phoneNumber,        LocalDate Booking_Date,        String LastName    ) {
        this.FirstName = FirstName;
        this.LeaveDate = LeaveDate;
        this.phoneNumber = phoneNumber;
        this.Booking_Date = Booking_Date;
        this.LastName = LastName;
    }


    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public LocalDate getLeavedate() {
        return LeaveDate;
    }

    public void setLeavedate(LocalDate LeaveDate) {
        this.LeaveDate = LeaveDate;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public LocalDate getBooking_date() {
        return Booking_Date;
    }

    public void setBooking_date(LocalDate Booking_Date) {
        this.Booking_Date = Booking_Date;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }


}