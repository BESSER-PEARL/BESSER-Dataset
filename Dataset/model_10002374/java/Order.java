





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String customername;
    private int shippingid;
    private int Orderid;
    private int datecreated;
    private int shippinddate;
    private int customerid;
    private String statues;





    private OnlineShopping onlineshopping;


    public Order(
        String customername,        int shippingid,        int Orderid,        int datecreated,        int shippinddate,        int customerid,        String statues    ) {
        this.customername = customername;
        this.shippingid = shippingid;
        this.Orderid = Orderid;
        this.datecreated = datecreated;
        this.shippinddate = shippinddate;
        this.customerid = customerid;
        this.statues = statues;
    }


    public String getCustomername() {
        return customername;
    }

    public void setCustomername(String customername) {
        this.customername = customername;
    }
    public int getShippingid() {
        return shippingid;
    }

    public void setShippingid(int shippingid) {
        this.shippingid = shippingid;
    }
    public int getOrderid() {
        return Orderid;
    }

    public void setOrderid(int Orderid) {
        this.Orderid = Orderid;
    }
    public int getDatecreated() {
        return datecreated;
    }

    public void setDatecreated(int datecreated) {
        this.datecreated = datecreated;
    }
    public int getShippinddate() {
        return shippinddate;
    }

    public void setShippinddate(int shippinddate) {
        this.shippinddate = shippinddate;
    }
    public int getCustomerid() {
        return customerid;
    }

    public void setCustomerid(int customerid) {
        this.customerid = customerid;
    }
    public String getStatues() {
        return statues;
    }

    public void setStatues(String statues) {
        this.statues = statues;
    }

    public OnlineShopping getOnlineshopping() {
        return onlineshopping;
    }

    public void setOnlineshopping(OnlineShopping onlineshopping) {
        this.onlineshopping = onlineshopping;
    }

}