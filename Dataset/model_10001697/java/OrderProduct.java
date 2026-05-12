





import java.util.List;
import java.util.ArrayList;

public class OrderProduct  {

    private None Oid;
    private None Pid;
    private int ID;





    private Products products;




    private List<Order> orders;


    public OrderProduct(
        None Oid,        None Pid,        int ID    ) {
        this.Oid = Oid;
        this.Pid = Pid;
        this.ID = ID;
        this.orders = new ArrayList<>();
    }

    public OrderProduct(
        None Oid,        None Pid,        int ID        ArrayList<Order> orders    ) {
        this.Oid = Oid;
        this.Pid = Pid;
        this.ID = ID;
        this.orders = orders;
    }

    public None getOid() {
        return Oid;
    }

    public void setOid(None Oid) {
        this.Oid = Oid;
    }
    public None getPid() {
        return Pid;
    }

    public void setPid(None Pid) {
        this.Pid = Pid;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Products getProducts() {
        return products;
    }

    public void setProducts(Products products) {
        this.products = products;
    }
    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}