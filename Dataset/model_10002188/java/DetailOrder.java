





import java.util.List;
import java.util.ArrayList;

public class DetailOrder  {

    private int DetailOrderID;
    private int ProductID;
    private String DetailOrderInfo;
    private int OrderID;





    private List<Products> productss;




    private Orders orders;


    public DetailOrder(
        int DetailOrderID,        int ProductID,        String DetailOrderInfo,        int OrderID    ) {
        this.DetailOrderID = DetailOrderID;
        this.ProductID = ProductID;
        this.DetailOrderInfo = DetailOrderInfo;
        this.OrderID = OrderID;
        this.productss = new ArrayList<>();
    }

    public DetailOrder(
        int DetailOrderID,        int ProductID,        String DetailOrderInfo,        int OrderID        ArrayList<Products> productss    ) {
        this.DetailOrderID = DetailOrderID;
        this.ProductID = ProductID;
        this.DetailOrderInfo = DetailOrderInfo;
        this.OrderID = OrderID;
        this.productss = productss;
    }

    public int getDetailorderid() {
        return DetailOrderID;
    }

    public void setDetailorderid(int DetailOrderID) {
        this.DetailOrderID = DetailOrderID;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public String getDetailorderinfo() {
        return DetailOrderInfo;
    }

    public void setDetailorderinfo(String DetailOrderInfo) {
        this.DetailOrderInfo = DetailOrderInfo;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }

    public List<Products> getProductss() {
        return productss;
    }

    public void addProducts(Products products) {
        this.productss.add(products);
    }
    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}