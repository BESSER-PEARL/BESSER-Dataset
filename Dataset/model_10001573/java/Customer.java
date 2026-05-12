





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private None type;
    private None DiscountSlab_list_;
    private None shoppingCart;





    private PremiumCustomer premiumcustomer;




    private ShoppingCart shoppingcart;




    private Customer customer;




    private List<Payment> payments;




    private List<Order> orders;




    private ShoppingCart shoppingcart;




    private CustomerHandler customerhandler;




    private PurchaseAmountSlab purchaseamountslab;


    public Customer(
        None type,        None DiscountSlab_list_,        None shoppingCart    ) {
        this.type = type;
        this.DiscountSlab_list_ = DiscountSlab_list_;
        this.shoppingCart = shoppingCart;
        this.payments = new ArrayList<>();
        this.orders = new ArrayList<>();
    }

    public Customer(
        None type,        None DiscountSlab_list_,        None shoppingCart        ArrayList<Payment> payments,        ArrayList<Order> orders    ) {
        this.type = type;
        this.DiscountSlab_list_ = DiscountSlab_list_;
        this.shoppingCart = shoppingCart;
        this.payments = payments;
        this.orders = orders;
    }

    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public None getDiscountslab_list_() {
        return DiscountSlab_list_;
    }

    public void setDiscountslab_list_(None DiscountSlab_list_) {
        this.DiscountSlab_list_ = DiscountSlab_list_;
    }
    public None getShoppingcart() {
        return shoppingCart;
    }

    public void setShoppingcart(None shoppingCart) {
        this.shoppingCart = shoppingCart;
    }

    public PremiumCustomer getPremiumcustomer() {
        return premiumcustomer;
    }

    public void setPremiumcustomer(PremiumCustomer premiumcustomer) {
        this.premiumcustomer = premiumcustomer;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public CustomerHandler getCustomerhandler() {
        return customerhandler;
    }

    public void setCustomerhandler(CustomerHandler customerhandler) {
        this.customerhandler = customerhandler;
    }
    public PurchaseAmountSlab getPurchaseamountslab() {
        return purchaseamountslab;
    }

    public void setPurchaseamountslab(PurchaseAmountSlab purchaseamountslab) {
        this.purchaseamountslab = purchaseamountslab;
    }

}