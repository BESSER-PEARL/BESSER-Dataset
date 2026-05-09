





import java.util.List;
import java.util.ArrayList;

public class newClasses_CreditCard  {

    private String cvc;
    private String year;
    private String month;
    private String creditCardNumber;
    private String firstName;
    private String lastName;





    private newClasses_Customer newclasses_customer;


    public newClasses_CreditCard(
        String cvc,        String year,        String month,        String creditCardNumber,        String firstName,        String lastName    ) {
        this.cvc = cvc;
        this.year = year;
        this.month = month;
        this.creditCardNumber = creditCardNumber;
        this.firstName = firstName;
        this.lastName = lastName;
    }


    public String getCvc() {
        return cvc;
    }

    public void setCvc(String cvc) {
        this.cvc = cvc;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getCreditcardnumber() {
        return creditCardNumber;
    }

    public void setCreditcardnumber(String creditCardNumber) {
        this.creditCardNumber = creditCardNumber;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }

    public newClasses_Customer getNewclasses_customer() {
        return newclasses_customer;
    }

    public void setNewclasses_customer(newClasses_Customer newclasses_customer) {
        this.newclasses_customer = newclasses_customer;
    }

}