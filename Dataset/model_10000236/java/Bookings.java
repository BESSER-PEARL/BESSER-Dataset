




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Bookings  {

    private LocalDate Date;
    private int People;
    private String CustomerName;
    private int BookingID;
    private int TableNo;
    private String Phone;
    private LocalDate Time;



    public Bookings(
        LocalDate Date,        int People,        String CustomerName,        int BookingID,        int TableNo,        String Phone,        LocalDate Time    ) {
        this.Date = Date;
        this.People = People;
        this.CustomerName = CustomerName;
        this.BookingID = BookingID;
        this.TableNo = TableNo;
        this.Phone = Phone;
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
    public int getTableno() {
        return TableNo;
    }

    public void setTableno(int TableNo) {
        this.TableNo = TableNo;
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


}