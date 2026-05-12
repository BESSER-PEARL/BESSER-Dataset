





import java.util.List;
import java.util.ArrayList;

public class Order1  {

    private int orderId;
    private None cust;
    private int conformationNo;
    private String deliveryDate;
    private String orderDate;
    private float totalAmount;





    private Customer1 customer1;


    public Order1(
        int orderId,        None cust,        int conformationNo,        String deliveryDate,        String orderDate,        float totalAmount    ) {
        this.orderId = orderId;
        this.cust = cust;
        this.conformationNo = conformationNo;
        this.deliveryDate = deliveryDate;
        this.orderDate = orderDate;
        this.totalAmount = totalAmount;
    }


    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }
    public None getCust() {
        return cust;
    }

    public void setCust(None cust) {
        this.cust = cust;
    }
    public int getConformationno() {
        return conformationNo;
    }

    public void setConformationno(int conformationNo) {
        this.conformationNo = conformationNo;
    }
    public String getDeliverydate() {
        return deliveryDate;
    }

    public void setDeliverydate(String deliveryDate) {
        this.deliveryDate = deliveryDate;
    }
    public String getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(String orderDate) {
        this.orderDate = orderDate;
    }
    public float getTotalamount() {
        return totalAmount;
    }

    public void setTotalamount(float totalAmount) {
        this.totalAmount = totalAmount;
    }

    public Customer1 getCustomer1() {
        return customer1;
    }

    public void setCustomer1(Customer1 customer1) {
        this.customer1 = customer1;
    }

}