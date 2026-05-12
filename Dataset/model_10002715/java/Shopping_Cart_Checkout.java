





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart_Checkout  {

    private int CheckoutID;
    private String billingMethod;
    private int Paymentid;
    private float Checkout__;
    private String CustomerID;





    private Shopping_Cart_ShoppingCart shopping_cart_shoppingcart;




    private List<Customer_Payment> customer_payments;


    public Shopping_Cart_Checkout(
        int CheckoutID,        String billingMethod,        int Paymentid,        float Checkout__,        String CustomerID    ) {
        this.CheckoutID = CheckoutID;
        this.billingMethod = billingMethod;
        this.Paymentid = Paymentid;
        this.Checkout__ = Checkout__;
        this.CustomerID = CustomerID;
        this.customer_payments = new ArrayList<>();
    }

    public Shopping_Cart_Checkout(
        int CheckoutID,        String billingMethod,        int Paymentid,        float Checkout__,        String CustomerID        ArrayList<Customer_Payment> customer_payments    ) {
        this.CheckoutID = CheckoutID;
        this.billingMethod = billingMethod;
        this.Paymentid = Paymentid;
        this.Checkout__ = Checkout__;
        this.CustomerID = CustomerID;
        this.customer_payments = customer_payments;
    }

    public int getCheckoutid() {
        return CheckoutID;
    }

    public void setCheckoutid(int CheckoutID) {
        this.CheckoutID = CheckoutID;
    }
    public String getBillingmethod() {
        return billingMethod;
    }

    public void setBillingmethod(String billingMethod) {
        this.billingMethod = billingMethod;
    }
    public int getPaymentid() {
        return Paymentid;
    }

    public void setPaymentid(int Paymentid) {
        this.Paymentid = Paymentid;
    }
    public float getCheckout__() {
        return Checkout__;
    }

    public void setCheckout__(float Checkout__) {
        this.Checkout__ = Checkout__;
    }
    public String getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(String CustomerID) {
        this.CustomerID = CustomerID;
    }

    public Shopping_Cart_ShoppingCart getShopping_cart_shoppingcart() {
        return shopping_cart_shoppingcart;
    }

    public void setShopping_cart_shoppingcart(Shopping_Cart_ShoppingCart shopping_cart_shoppingcart) {
        this.shopping_cart_shoppingcart = shopping_cart_shoppingcart;
    }
    public List<Customer_Payment> getCustomer_payments() {
        return customer_payments;
    }

    public void addCustomer_payment(Customer_payment customer_payment) {
        this.customer_payments.add(customer_payment);
    }

}