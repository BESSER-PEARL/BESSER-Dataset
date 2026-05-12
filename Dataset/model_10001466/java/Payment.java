





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String paymentID;
    private String paymentDate;
    private String paymentAmount;
    private String PaymentType;
    private String PaymentStatus;





    private Orders orders;




    private Customer customer;


    public Payment(
        String paymentID,        String paymentDate,        String paymentAmount,        String PaymentType,        String PaymentStatus    ) {
        this.paymentID = paymentID;
        this.paymentDate = paymentDate;
        this.paymentAmount = paymentAmount;
        this.PaymentType = PaymentType;
        this.PaymentStatus = PaymentStatus;
    }


    public String getPaymentid() {
        return paymentID;
    }

    public void setPaymentid(String paymentID) {
        this.paymentID = paymentID;
    }
    public String getPaymentdate() {
        return paymentDate;
    }

    public void setPaymentdate(String paymentDate) {
        this.paymentDate = paymentDate;
    }
    public String getPaymentamount() {
        return paymentAmount;
    }

    public void setPaymentamount(String paymentAmount) {
        this.paymentAmount = paymentAmount;
    }
    public String getPaymenttype() {
        return PaymentType;
    }

    public void setPaymenttype(String PaymentType) {
        this.PaymentType = PaymentType;
    }
    public String getPaymentstatus() {
        return PaymentStatus;
    }

    public void setPaymentstatus(String PaymentStatus) {
        this.PaymentStatus = PaymentStatus;
    }

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}