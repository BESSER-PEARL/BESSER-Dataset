





import java.util.List;
import java.util.ArrayList;

public class BookingController  {

    private String Time;
    private String CustomerName;
    private String Phone;
    private String Date;
    private int BookingID;
    private String TableNo;



    public BookingController(
        String Time,        String CustomerName,        String Phone,        String Date,        int BookingID,        String TableNo    ) {
        this.Time = Time;
        this.CustomerName = CustomerName;
        this.Phone = Phone;
        this.Date = Date;
        this.BookingID = BookingID;
        this.TableNo = TableNo;
    }


    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
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
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public int getBookingid() {
        return BookingID;
    }

    public void setBookingid(int BookingID) {
        this.BookingID = BookingID;
    }
    public String getTableno() {
        return TableNo;
    }

    public void setTableno(String TableNo) {
        this.TableNo = TableNo;
    }


}