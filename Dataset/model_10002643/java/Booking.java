





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private int type;
    private String booking_Id;
    private String contact;
    private String date;
    private String reservedTables;
    private String name;





    private RMS rms;


    public Booking(
        int type,        String booking_Id,        String contact,        String date,        String reservedTables,        String name    ) {
        this.type = type;
        this.booking_Id = booking_Id;
        this.contact = contact;
        this.date = date;
        this.reservedTables = reservedTables;
        this.name = name;
    }


    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getBooking_id() {
        return booking_Id;
    }

    public void setBooking_id(String booking_Id) {
        this.booking_Id = booking_Id;
    }
    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RMS getRms() {
        return rms;
    }

    public void setRms(RMS rms) {
        this.rms = rms;
    }

}