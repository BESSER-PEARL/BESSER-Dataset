





import java.util.List;
import java.util.ArrayList;

public class Cart_Checkout  {

    private int Paymentid;
    private None PayBill__;
    private String billingMethod;
    private String CustomerID;
    private int CheckoutID;





    private Cart_ShoppingCart cart_shoppingcart;




    private List<Customer_Payment1> customer_payment1s;


    public Cart_Checkout(
        int Paymentid,        None PayBill__,        String billingMethod,        String CustomerID,        int CheckoutID    ) {
        this.Paymentid = Paymentid;
        this.PayBill__ = PayBill__;
        this.billingMethod = billingMethod;
        this.CustomerID = CustomerID;
        this.CheckoutID = CheckoutID;
        this.customer_payment1s = new ArrayList<>();
    }

    public Cart_Checkout(
        int Paymentid,        None PayBill__,        String billingMethod,        String CustomerID,        int CheckoutID        ArrayList<Customer_Payment1> customer_payment1s    ) {
        this.Paymentid = Paymentid;
        this.PayBill__ = PayBill__;
        this.billingMethod = billingMethod;
        this.CustomerID = CustomerID;
        this.CheckoutID = CheckoutID;
        this.customer_payment1s = customer_payment1s;
    }

    public int getPaymentid() {
        return Paymentid;
    }

    public void setPaymentid(int Paymentid) {
        this.Paymentid = Paymentid;
    }
    public None getPaybill__() {
        return PayBill__;
    }

    public void setPaybill__(None PayBill__) {
        this.PayBill__ = PayBill__;
    }
    public String getBillingmethod() {
        return billingMethod;
    }

    public void setBillingmethod(String billingMethod) {
        this.billingMethod = billingMethod;
    }
    public String getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(String CustomerID) {
        this.CustomerID = CustomerID;
    }
    public int getCheckoutid() {
        return CheckoutID;
    }

    public void setCheckoutid(int CheckoutID) {
        this.CheckoutID = CheckoutID;
    }

    public Cart_ShoppingCart getCart_shoppingcart() {
        return cart_shoppingcart;
    }

    public void setCart_shoppingcart(Cart_ShoppingCart cart_shoppingcart) {
        this.cart_shoppingcart = cart_shoppingcart;
    }
    public List<Customer_Payment1> getCustomer_payment1s() {
        return customer_payment1s;
    }

    public void addCustomer_payment1(Customer_payment1 customer_payment1) {
        this.customer_payment1s.add(customer_payment1);
    }

}