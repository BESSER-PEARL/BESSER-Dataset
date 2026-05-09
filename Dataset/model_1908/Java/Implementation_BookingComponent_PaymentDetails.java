





import java.util.List;
import java.util.ArrayList;

public class Implementation_BookingComponent_PaymentDetails  {

    private String lastName;
    private String ccNumber;
    private String address;
    private String firstName;
    private String expiryYear;
    private String ccv;
    private String expiryMonth;



    public Implementation_BookingComponent_PaymentDetails(
        String lastName,        String ccNumber,        String address,        String firstName,        String expiryYear,        String ccv,        String expiryMonth    ) {
        this.lastName = lastName;
        this.ccNumber = ccNumber;
        this.address = address;
        this.firstName = firstName;
        this.expiryYear = expiryYear;
        this.ccv = ccv;
        this.expiryMonth = expiryMonth;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getCcnumber() {
        return ccNumber;
    }

    public void setCcnumber(String ccNumber) {
        this.ccNumber = ccNumber;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getExpiryyear() {
        return expiryYear;
    }

    public void setExpiryyear(String expiryYear) {
        this.expiryYear = expiryYear;
    }
    public String getCcv() {
        return ccv;
    }

    public void setCcv(String ccv) {
        this.ccv = ccv;
    }
    public String getExpirymonth() {
        return expiryMonth;
    }

    public void setExpirymonth(String expiryMonth) {
        this.expiryMonth = expiryMonth;
    }


}