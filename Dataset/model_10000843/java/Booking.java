





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private String date;
    private String contact;
    private String name;
    private int type;
    private String reservedTables;
    private String booking_Id;





    private RMS rms;


    public Booking(
        String date,        String contact,        String name,        int type,        String reservedTables,        String booking_Id    ) {
        this.date = date;
        this.contact = contact;
        this.name = name;
        this.type = type;
        this.reservedTables = reservedTables;
        this.booking_Id = booking_Id;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
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