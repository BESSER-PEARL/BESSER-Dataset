




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Models_Order  {

    private int shippingInfoId;
    private LocalDate dateCreated;
    private int customerid;
    private String dateShipped;
    private int orderID;
    private String status;





    private List<Models_LineItem> models_lineitems;




    private Models_Customer models_customer;




    private dao_OrderDao_Interface dao_orderdao_interface;


    public Models_Order(
        int shippingInfoId,        LocalDate dateCreated,        int customerid,        String dateShipped,        int orderID,        String status    ) {
        this.shippingInfoId = shippingInfoId;
        this.dateCreated = dateCreated;
        this.customerid = customerid;
        this.dateShipped = dateShipped;
        this.orderID = orderID;
        this.status = status;
        this.models_lineitems = new ArrayList<>();
    }

    public Models_Order(
        int shippingInfoId,        LocalDate dateCreated,        int customerid,        String dateShipped,        int orderID,        String status        ArrayList<Models_LineItem> models_lineitems    ) {
        this.shippingInfoId = shippingInfoId;
        this.dateCreated = dateCreated;
        this.customerid = customerid;
        this.dateShipped = dateShipped;
        this.orderID = orderID;
        this.status = status;
        this.models_lineitems = models_lineitems;
    }

    public int getShippinginfoid() {
        return shippingInfoId;
    }

    public void setShippinginfoid(int shippingInfoId) {
        this.shippingInfoId = shippingInfoId;
    }
    public LocalDate getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(LocalDate dateCreated) {
        this.dateCreated = dateCreated;
    }
    public int getCustomerid() {
        return customerid;
    }

    public void setCustomerid(int customerid) {
        this.customerid = customerid;
    }
    public String getDateshipped() {
        return dateShipped;
    }

    public void setDateshipped(String dateShipped) {
        this.dateShipped = dateShipped;
    }
    public int getOrderid() {
        return orderID;
    }

    public void setOrderid(int orderID) {
        this.orderID = orderID;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public List<Models_LineItem> getModels_lineitems() {
        return models_lineitems;
    }

    public void addModels_lineitem(Models_lineitem models_lineitem) {
        this.models_lineitems.add(models_lineitem);
    }
    public Models_Customer getModels_customer() {
        return models_customer;
    }

    public void setModels_customer(Models_Customer models_customer) {
        this.models_customer = models_customer;
    }
    public dao_OrderDao_Interface getDao_orderdao_interface() {
        return dao_orderdao_interface;
    }

    public void setDao_orderdao_interface(dao_OrderDao_Interface dao_orderdao_interface) {
        this.dao_orderdao_interface = dao_orderdao_interface;
    }

}