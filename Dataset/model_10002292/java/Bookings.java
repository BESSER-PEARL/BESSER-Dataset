




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Bookings  {

    private int People;
    private String Phone;
    private String CustomerName;
    private int BookingID;
    private int TableNo;
    private LocalDate Time;
    private LocalDate Date;



    public Bookings(
        int People,        String Phone,        String CustomerName,        int BookingID,        int TableNo,        LocalDate Time,        LocalDate Date    ) {
        this.People = People;
        this.Phone = Phone;
        this.CustomerName = CustomerName;
        this.BookingID = BookingID;
        this.TableNo = TableNo;
        this.Time = Time;
        this.Date = Date;
    }


    public int getPeople() {
        return People;
    }

    public void setPeople(int People) {
        this.People = People;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
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


}