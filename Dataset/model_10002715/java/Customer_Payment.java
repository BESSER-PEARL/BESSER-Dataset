





import java.util.List;
import java.util.ArrayList;

public class Customer_Payment  {

    private int PayPal;
    private int ApplPay;
    private String CustomerId;
    private int Paymentid;
    private float Payment__;
    private String login;





    private Customer_Customer customer_customer;


    public Customer_Payment(
        int PayPal,        int ApplPay,        String CustomerId,        int Paymentid,        float Payment__,        String login    ) {
        this.PayPal = PayPal;
        this.ApplPay = ApplPay;
        this.CustomerId = CustomerId;
        this.Paymentid = Paymentid;
        this.Payment__ = Payment__;
        this.login = login;
    }


    public int getPaypal() {
        return PayPal;
    }

    public void setPaypal(int PayPal) {
        this.PayPal = PayPal;
    }
    public int getApplpay() {
        return ApplPay;
    }

    public void setApplpay(int ApplPay) {
        this.ApplPay = ApplPay;
    }
    public String getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(String CustomerId) {
        this.CustomerId = CustomerId;
    }
    public int getPaymentid() {
        return Paymentid;
    }

    public void setPaymentid(int Paymentid) {
        this.Paymentid = Paymentid;
    }
    public float getPayment__() {
        return Payment__;
    }

    public void setPayment__(float Payment__) {
        this.Payment__ = Payment__;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public Customer_Customer getCustomer_customer() {
        return customer_customer;
    }

    public void setCustomer_customer(Customer_Customer customer_customer) {
        this.customer_customer = customer_customer;
    }

}