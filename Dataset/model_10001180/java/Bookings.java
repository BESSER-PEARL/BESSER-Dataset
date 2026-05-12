




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Bookings  {

    private LocalDate Time;
    private String Phone;
    private int BookingID;
    private String CustomerName;
    private int People;
    private LocalDate Date;



    public Bookings(
        LocalDate Time,        String Phone,        int BookingID,        String CustomerName,        int People,        LocalDate Date    ) {
        this.Time = Time;
        this.Phone = Phone;
        this.BookingID = BookingID;
        this.CustomerName = CustomerName;
        this.People = People;
        this.Date = Date;
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
    public int getBookingid() {
        return BookingID;
    }

    public void setBookingid(int BookingID) {
        this.BookingID = BookingID;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
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