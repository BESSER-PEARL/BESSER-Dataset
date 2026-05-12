





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String ShippingAddress;
    private String customerId;
    private String status;
    private int OrderId;
    private String dateShipped;
    private String dateCreated;
    private String Payment;
    private String OrderStatus;
    private String customerName;
    private String Item;
    private String BillingAddress;





    private Payment_Interface payment_interface;




    private Address address;




    private Payment payment;




    private Customer customer;




    private Administrator administrator;




    private Item item;




    private OrderService orderservice;


    public Order(
        String ShippingAddress,        String customerId,        String status,        int OrderId,        String dateShipped,        String dateCreated,        String Payment,        String OrderStatus,        String customerName,        String Item,        String BillingAddress    ) {
        this.ShippingAddress = ShippingAddress;
        this.customerId = customerId;
        this.status = status;
        this.OrderId = OrderId;
        this.dateShipped = dateShipped;
        this.dateCreated = dateCreated;
        this.Payment = Payment;
        this.OrderStatus = OrderStatus;
        this.customerName = customerName;
        this.Item = Item;
        this.BillingAddress = BillingAddress;
    }


    public String getShippingaddress() {
        return ShippingAddress;
    }

    public void setShippingaddress(String ShippingAddress) {
        this.ShippingAddress = ShippingAddress;
    }
    public String getCustomerid() {
        return customerId;
    }

    public void setCustomerid(String customerId) {
        this.customerId = customerId;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getOrderid() {
        return OrderId;
    }

    public void setOrderid(int OrderId) {
        this.OrderId = OrderId;
    }
    public String getDateshipped() {
        return dateShipped;
    }

    public void setDateshipped(String dateShipped) {
        this.dateShipped = dateShipped;
    }
    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
    }
    public String getPayment() {
        return Payment;
    }

    public void setPayment(String Payment) {
        this.Payment = Payment;
    }
    public String getOrderstatus() {
        return OrderStatus;
    }

    public void setOrderstatus(String OrderStatus) {
        this.OrderStatus = OrderStatus;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }
    public String getItem() {
        return Item;
    }

    public void setItem(String Item) {
        this.Item = Item;
    }
    public String getBillingaddress() {
        return BillingAddress;
    }

    public void setBillingaddress(String BillingAddress) {
        this.BillingAddress = BillingAddress;
    }

    public Payment_Interface getPayment_interface() {
        return payment_interface;
    }

    public void setPayment_interface(Payment_Interface payment_interface) {
        this.payment_interface = payment_interface;
    }
    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }
    public OrderService getOrderservice() {
        return orderservice;
    }

    public void setOrderservice(OrderService orderservice) {
        this.orderservice = orderservice;
    }

}