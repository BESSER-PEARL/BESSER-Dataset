





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String name;
    private String reservedTables;
    private String contact;
    private int type;
    private String date;
    private String booking_Id;





    private RMS rms;


    public Booking(
        String name,        String reservedTables,        String contact,        int type,        String date,        String booking_Id    ) {
        this.name = name;
        this.reservedTables = reservedTables;
        this.contact = contact;
        this.type = type;
        this.date = date;
        this.booking_Id = booking_Id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }
    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getBooking_id() {
        return booking_Id;
    }

    public void setBooking_id(String booking_Id) {
        this.booking_Id = booking_Id;
    }

    public RMS getRms() {
        return rms;
    }

    public void setRms(RMS rms) {
        this.rms = rms;
    }

}