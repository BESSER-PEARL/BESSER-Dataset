




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_Bookings_Booking  {

    private String requests;
    private LocalDate issueDate;
    private String bookedStays;
    private String customer;
    private String nbrGuests;
    private String bookingNbr;





    private CreditCard creditcard;


    public Classes_Bookings_Booking(
        String requests,        LocalDate issueDate,        String bookedStays,        String customer,        String nbrGuests,        String bookingNbr    ) {
        this.requests = requests;
        this.issueDate = issueDate;
        this.bookedStays = bookedStays;
        this.customer = customer;
        this.nbrGuests = nbrGuests;
        this.bookingNbr = bookingNbr;
    }


    public String getRequests() {
        return requests;
    }

    public void setRequests(String requests) {
        this.requests = requests;
    }
    public LocalDate getIssuedate() {
        return issueDate;
    }

    public void setIssuedate(LocalDate issueDate) {
        this.issueDate = issueDate;
    }
    public String getBookedstays() {
        return bookedStays;
    }

    public void setBookedstays(String bookedStays) {
        this.bookedStays = bookedStays;
    }
    public String getCustomer() {
        return customer;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }
    public String getNbrguests() {
        return nbrGuests;
    }

    public void setNbrguests(String nbrGuests) {
        this.nbrGuests = nbrGuests;
    }
    public String getBookingnbr() {
        return bookingNbr;
    }

    public void setBookingnbr(String bookingNbr) {
        this.bookingNbr = bookingNbr;
    }

    public CreditCard getCreditcard() {
        return creditcard;
    }

    public void setCreditcard(CreditCard creditcard) {
        this.creditcard = creditcard;
    }

}