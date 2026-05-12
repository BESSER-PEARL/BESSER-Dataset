




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Bookings  {

    private int BookingID;
    private LocalDate Time;
    private LocalDate Date;
    private int People;
    private int TableNo;
    private String CustomerName;
    private String Phone;



    public Bookings(
        int BookingID,        LocalDate Time,        LocalDate Date,        int People,        int TableNo,        String CustomerName,        String Phone    ) {
        this.BookingID = BookingID;
        this.Time = Time;
        this.Date = Date;
        this.People = People;
        this.TableNo = TableNo;
        this.CustomerName = CustomerName;
        this.Phone = Phone;
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
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public int getPeople() {
        return People;
    }

    public void setPeople(int People) {
        this.People = People;
    }
    public int getTableno() {
        return TableNo;
    }

    public void setTableno(int TableNo) {
        this.TableNo = TableNo;
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


}