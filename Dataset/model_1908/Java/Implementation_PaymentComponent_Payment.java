





import java.util.List;
import java.util.ArrayList;

public class Implementation_PaymentComponent_Payment  {

    private String firstName;
    private String expiryYear;
    private String lastName;
    private String ccNumber;
    private float amount;
    private String ccv;
    private String expiryMonth;





    private Implementation_PaymentComponent_PaymentHandler implementation_paymentcomponent_paymenthandler;


    public Implementation_PaymentComponent_Payment(
        String firstName,        String expiryYear,        String lastName,        String ccNumber,        float amount,        String ccv,        String expiryMonth    ) {
        this.firstName = firstName;
        this.expiryYear = expiryYear;
        this.lastName = lastName;
        this.ccNumber = ccNumber;
        this.amount = amount;
        this.ccv = ccv;
        this.expiryMonth = expiryMonth;
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
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
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

    public Implementation_PaymentComponent_PaymentHandler getImplementation_paymentcomponent_paymenthandler() {
        return implementation_paymentcomponent_paymenthandler;
    }

    public void setImplementation_paymentcomponent_paymenthandler(Implementation_PaymentComponent_PaymentHandler implementation_paymentcomponent_paymenthandler) {
        this.implementation_paymentcomponent_paymenthandler = implementation_paymentcomponent_paymenthandler;
    }

}