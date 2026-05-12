





import java.util.List;
import java.util.ArrayList;

public class Online_Order_and_CC_Processing  {

    private String order;
    private String payment;
    private boolean paymentApproved;





    private Customer customer;


    public Online_Order_and_CC_Processing(
        String order,        String payment,        boolean paymentApproved    ) {
        this.order = order;
        this.payment = payment;
        this.paymentApproved = paymentApproved;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }
    public String getPayment() {
        return payment;
    }

    public void setPayment(String payment) {
        this.payment = payment;
    }
    public boolean getPaymentapproved() {
        return paymentApproved;
    }

    public void setPaymentapproved(boolean paymentApproved) {
        this.paymentApproved = paymentApproved;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}