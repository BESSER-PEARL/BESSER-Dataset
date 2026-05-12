




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Bookings  {

    private String CustomerName;
    private String Phone;
    private LocalDate Time;
    private int BookingID;
    private int People;
    private LocalDate Date;



    public Bookings(
        String CustomerName,        String Phone,        LocalDate Time,        int BookingID,        int People,        LocalDate Date    ) {
        this.CustomerName = CustomerName;
        this.Phone = Phone;
        this.Time = Time;
        this.BookingID = BookingID;
        this.People = People;
        this.Date = Date;
    }


    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public LocalDate getTime() {
        return Time;
    }

    public void setTime(LocalDate Time) {
        this.Time = Time;
    }
    public int getBookingid() {
        return BookingID;
    }

    public void setBookingid(int BookingID) {
        this.BookingID = BookingID;
    }
    public int getPeople() {
        return People;
    }

    public void setPeople(int People) {
        this.People = People;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }


}