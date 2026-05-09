




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_Stays_Stay  {

    private String bills;
    private LocalDate fromDate;
    private String checkedInGuests;
    private String checkedOutGuests;
    private String ID;
    private String booking;
    private String bookable;
    private LocalDate toDate;



    public Classes_Stays_Stay(
        String bills,        LocalDate fromDate,        String checkedInGuests,        String checkedOutGuests,        String ID,        String booking,        String bookable,        LocalDate toDate    ) {
        this.bills = bills;
        this.fromDate = fromDate;
        this.checkedInGuests = checkedInGuests;
        this.checkedOutGuests = checkedOutGuests;
        this.ID = ID;
        this.booking = booking;
        this.bookable = bookable;
        this.toDate = toDate;
    }


    public String getBills() {
        return bills;
    }

    public void setBills(String bills) {
        this.bills = bills;
    }
    public LocalDate getFromdate() {
        return fromDate;
    }

    public void setFromdate(LocalDate fromDate) {
        this.fromDate = fromDate;
    }
    public String getCheckedinguests() {
        return checkedInGuests;
    }

    public void setCheckedinguests(String checkedInGuests) {
        this.checkedInGuests = checkedInGuests;
    }
    public String getCheckedoutguests() {
        return checkedOutGuests;
    }

    public void setCheckedoutguests(String checkedOutGuests) {
        this.checkedOutGuests = checkedOutGuests;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getBooking() {
        return booking;
    }

    public void setBooking(String booking) {
        this.booking = booking;
    }
    public String getBookable() {
        return bookable;
    }

    public void setBookable(String bookable) {
        this.bookable = bookable;
    }
    public LocalDate getTodate() {
        return toDate;
    }

    public void setTodate(LocalDate toDate) {
        this.toDate = toDate;
    }


}