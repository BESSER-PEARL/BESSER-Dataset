




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Bookings  {

    private LocalDate Date;
    private String CustomerName;
    private int BookingID;
    private LocalDate Time;
    private String Phone;
    private int People;



    public Bookings(
        LocalDate Date,        String CustomerName,        int BookingID,        LocalDate Time,        String Phone,        int People    ) {
        this.Date = Date;
        this.CustomerName = CustomerName;
        this.BookingID = BookingID;
        this.Time = Time;
        this.Phone = Phone;
        this.People = People;
    }


    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public int getBookingid() {
        return BookingID;
    }

    public void setBookingid(int BookingID) {
        this.BookingID = BookingID;
    }
    public LocalDate getTime() {
        return Time;
    }

    public void setTime(LocalDate Time) {
        this.Time = Time;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public int getPeople() {
        return People;
    }

    public void setPeople(int People) {
        this.People = People;
    }


}