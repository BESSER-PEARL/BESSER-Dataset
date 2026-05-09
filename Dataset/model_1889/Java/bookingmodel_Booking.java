





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_Booking  {

    private String endDate;
    private String serviceNotes;
    private String startDate;
    private String nrOfGuests;
    private String paymentMethod;
    private String bookingRef;
    private String isPayed;





    private List<bookingmodel_RoomToGuestIDEntry> bookingmodel_roomtoguestidentrys;


    public bookingmodel_Booking(
        String endDate,        String serviceNotes,        String startDate,        String nrOfGuests,        String paymentMethod,        String bookingRef,        String isPayed    ) {
        this.endDate = endDate;
        this.serviceNotes = serviceNotes;
        this.startDate = startDate;
        this.nrOfGuests = nrOfGuests;
        this.paymentMethod = paymentMethod;
        this.bookingRef = bookingRef;
        this.isPayed = isPayed;
        this.bookingmodel_roomtoguestidentrys = new ArrayList<>();
    }

    public bookingmodel_Booking(
        String endDate,        String serviceNotes,        String startDate,        String nrOfGuests,        String paymentMethod,        String bookingRef,        String isPayed        ArrayList<bookingmodel_RoomToGuestIDEntry> bookingmodel_roomtoguestidentrys    ) {
        this.endDate = endDate;
        this.serviceNotes = serviceNotes;
        this.startDate = startDate;
        this.nrOfGuests = nrOfGuests;
        this.paymentMethod = paymentMethod;
        this.bookingRef = bookingRef;
        this.isPayed = isPayed;
        this.bookingmodel_roomtoguestidentrys = bookingmodel_roomtoguestidentrys;
    }

    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getServicenotes() {
        return serviceNotes;
    }

    public void setServicenotes(String serviceNotes) {
        this.serviceNotes = serviceNotes;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public String getNrofguests() {
        return nrOfGuests;
    }

    public void setNrofguests(String nrOfGuests) {
        this.nrOfGuests = nrOfGuests;
    }
    public String getPaymentmethod() {
        return paymentMethod;
    }

    public void setPaymentmethod(String paymentMethod) {
        this.paymentMethod = paymentMethod;
    }
    public String getBookingref() {
        return bookingRef;
    }

    public void setBookingref(String bookingRef) {
        this.bookingRef = bookingRef;
    }
    public String getIspayed() {
        return isPayed;
    }

    public void setIspayed(String isPayed) {
        this.isPayed = isPayed;
    }

    public List<bookingmodel_RoomToGuestIDEntry> getBookingmodel_roomtoguestidentrys() {
        return bookingmodel_roomtoguestidentrys;
    }

    public void addBookingmodel_roomtoguestidentry(Bookingmodel_roomtoguestidentry bookingmodel_roomtoguestidentry) {
        this.bookingmodel_roomtoguestidentrys.add(bookingmodel_roomtoguestidentry);
    }

}