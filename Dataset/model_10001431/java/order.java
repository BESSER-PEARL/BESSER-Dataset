





import java.util.List;
import java.util.ArrayList;

public class order  {

    private int orderid;
    private String orderdate;
    private int price;





    private menu menu;


    public order(
        int orderid,        String orderdate,        int price    ) {
        this.orderid = orderid;
        this.orderdate = orderdate;
        this.price = price;
    }


    public int getOrderid() {
        return orderid;
    }

    public void setOrderid(int orderid) {
        this.orderid = orderid;
    }
    public String getOrderdate() {
        return orderdate;
    }

    public void setOrderdate(String orderdate) {
        this.orderdate = orderdate;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public menu getMenu() {
        return menu;
    }

    public void setMenu(menu menu) {
        this.menu = menu;
    }

}