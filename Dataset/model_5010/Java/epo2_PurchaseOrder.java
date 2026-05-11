





import java.util.List;
import java.util.ArrayList;

public class epo2_PurchaseOrder  {

    private String comment;
    private String orderDate;
    private String status;
    private int totalAmount;





    private epo2_PurchaseOrder epo2_purchaseorder;




    private epo2_Item epo2_item;




    private List<epo2_Item> epo2_items;


    public epo2_PurchaseOrder(
        String comment,        String orderDate,        String status,        int totalAmount    ) {
        this.comment = comment;
        this.orderDate = orderDate;
        this.status = status;
        this.totalAmount = totalAmount;
        this.epo2_items = new ArrayList<>();
    }

    public epo2_PurchaseOrder(
        String comment,        String orderDate,        String status,        int totalAmount        ArrayList<epo2_Item> epo2_items    ) {
        this.comment = comment;
        this.orderDate = orderDate;
        this.status = status;
        this.totalAmount = totalAmount;
        this.epo2_items = epo2_items;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(String orderDate) {
        this.orderDate = orderDate;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getTotalamount() {
        return totalAmount;
    }

    public void setTotalamount(int totalAmount) {
        this.totalAmount = totalAmount;
    }

    public epo2_PurchaseOrder getEpo2_purchaseorder() {
        return epo2_purchaseorder;
    }

    public void setEpo2_purchaseorder(epo2_PurchaseOrder epo2_purchaseorder) {
        this.epo2_purchaseorder = epo2_purchaseorder;
    }
    public epo2_Item getEpo2_item() {
        return epo2_item;
    }

    public void setEpo2_item(epo2_Item epo2_item) {
        this.epo2_item = epo2_item;
    }
    public List<epo2_Item> getEpo2_items() {
        return epo2_items;
    }

    public void addEpo2_item(Epo2_item epo2_item) {
        this.epo2_items.add(epo2_item);
    }

}