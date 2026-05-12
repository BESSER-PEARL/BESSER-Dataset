





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String status;
    private int orderTotalAmount;
    private int deliveryDate;
    private String orderedOn;
    private int shippingId;
    private int noOfItem;
    private None items;
    private int orderId;





    private Customer customer;




    private List<Product> products;


    public Order(
        String status,        int orderTotalAmount,        int deliveryDate,        String orderedOn,        int shippingId,        int noOfItem,        None items,        int orderId    ) {
        this.status = status;
        this.orderTotalAmount = orderTotalAmount;
        this.deliveryDate = deliveryDate;
        this.orderedOn = orderedOn;
        this.shippingId = shippingId;
        this.noOfItem = noOfItem;
        this.items = items;
        this.orderId = orderId;
        this.products = new ArrayList<>();
    }

    public Order(
        String status,        int orderTotalAmount,        int deliveryDate,        String orderedOn,        int shippingId,        int noOfItem,        None items,        int orderId        ArrayList<Product> products    ) {
        this.status = status;
        this.orderTotalAmount = orderTotalAmount;
        this.deliveryDate = deliveryDate;
        this.orderedOn = orderedOn;
        this.shippingId = shippingId;
        this.noOfItem = noOfItem;
        this.items = items;
        this.orderId = orderId;
        this.products = products;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getOrdertotalamount() {
        return orderTotalAmount;
    }

    public void setOrdertotalamount(int orderTotalAmount) {
        this.orderTotalAmount = orderTotalAmount;
    }
    public int getDeliverydate() {
        return deliveryDate;
    }

    public void setDeliverydate(int deliveryDate) {
        this.deliveryDate = deliveryDate;
    }
    public String getOrderedon() {
        return orderedOn;
    }

    public void setOrderedon(String orderedOn) {
        this.orderedOn = orderedOn;
    }
    public int getShippingid() {
        return shippingId;
    }

    public void setShippingid(int shippingId) {
        this.shippingId = shippingId;
    }
    public int getNoofitem() {
        return noOfItem;
    }

    public void setNoofitem(int noOfItem) {
        this.noOfItem = noOfItem;
    }
    public None getItems() {
        return items;
    }

    public void setItems(None items) {
        this.items = items;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}