





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_PaymentDetails  {

    private String expMonth;
    private String expYear;
    private String lastName;
    private String ccNr;
    private String ccV;
    private String firstName;





    private bookingmodel_Customer bookingmodel_customer;


    public bookingmodel_PaymentDetails(
        String expMonth,        String expYear,        String lastName,        String ccNr,        String ccV,        String firstName    ) {
        this.expMonth = expMonth;
        this.expYear = expYear;
        this.lastName = lastName;
        this.ccNr = ccNr;
        this.ccV = ccV;
        this.firstName = firstName;
    }


    public String getExpmonth() {
        return expMonth;
    }

    public void setExpmonth(String expMonth) {
        this.expMonth = expMonth;
    }
    public String getExpyear() {
        return expYear;
    }

    public void setExpyear(String expYear) {
        this.expYear = expYear;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getCcnr() {
        return ccNr;
    }

    public void setCcnr(String ccNr) {
        this.ccNr = ccNr;
    }
    public String getCcv() {
        return ccV;
    }

    public void setCcv(String ccV) {
        this.ccV = ccV;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }

    public bookingmodel_Customer getBookingmodel_customer() {
        return bookingmodel_customer;
    }

    public void setBookingmodel_customer(bookingmodel_Customer bookingmodel_customer) {
        this.bookingmodel_customer = bookingmodel_customer;
    }

}