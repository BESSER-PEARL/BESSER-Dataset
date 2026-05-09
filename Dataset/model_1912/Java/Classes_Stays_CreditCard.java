





import java.util.List;
import java.util.ArrayList;

public class Classes_Stays_CreditCard  {

    private String lastName;
    private String ccNumber;
    private String firstName;
    private String ccv;
    private String expiryYear;
    private String expiryMonth;



    public Classes_Stays_CreditCard(
        String lastName,        String ccNumber,        String firstName,        String ccv,        String expiryYear,        String expiryMonth    ) {
        this.lastName = lastName;
        this.ccNumber = ccNumber;
        this.firstName = firstName;
        this.ccv = ccv;
        this.expiryYear = expiryYear;
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
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getCcv() {
        return ccv;
    }

    public void setCcv(String ccv) {
        this.ccv = ccv;
    }
    public String getExpiryyear() {
        return expiryYear;
    }

    public void setExpiryyear(String expiryYear) {
        this.expiryYear = expiryYear;
    }
    public String getExpirymonth() {
        return expiryMonth;
    }

    public void setExpirymonth(String expiryMonth) {
        this.expiryMonth = expiryMonth;
    }


}