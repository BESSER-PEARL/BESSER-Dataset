





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String name;
    private String date;
    private int type;
    private String booking_Id;
    private String contact;
    private String reservedTables;





    private RMS rms;


    public Booking(
        String name,        String date,        int type,        String booking_Id,        String contact,        String reservedTables    ) {
        this.name = name;
        this.date = date;
        this.type = type;
        this.booking_Id = booking_Id;
        this.contact = contact;
        this.reservedTables = reservedTables;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
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
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }

    public RMS getRms() {
        return rms;
    }

    public void setRms(RMS rms) {
        this.rms = rms;
    }

}