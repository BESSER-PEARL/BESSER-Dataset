





import java.util.List;
import java.util.ArrayList;

public class extendedPO2_PurchaseOrder  {

    private String comment;
    private int totalAmount;
    private String orderDate;
    private String status;





    private extendedPO2_Customer extendedpo2_customer;




    private extendedPO2_PurchaseOrder extendedpo2_purchaseorder;




    private extendedPO2_Item extendedpo2_item;




    private extendedPO2_Address extendedpo2_address;




    private extendedPO2_Customer extendedpo2_customer;




    private extendedPO2_Address extendedpo2_address;




    private List<extendedPO2_Item> extendedpo2_items;


    public extendedPO2_PurchaseOrder(
        String comment,        int totalAmount,        String orderDate,        String status    ) {
        this.comment = comment;
        this.totalAmount = totalAmount;
        this.orderDate = orderDate;
        this.status = status;
        this.extendedpo2_items = new ArrayList<>();
    }

    public extendedPO2_PurchaseOrder(
        String comment,        int totalAmount,        String orderDate,        String status        ArrayList<extendedPO2_Item> extendedpo2_items    ) {
        this.comment = comment;
        this.totalAmount = totalAmount;
        this.orderDate = orderDate;
        this.status = status;
        this.extendedpo2_items = extendedpo2_items;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getTotalamount() {
        return totalAmount;
    }

    public void setTotalamount(int totalAmount) {
        this.totalAmount = totalAmount;
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

    public extendedPO2_Customer getExtendedpo2_customer() {
        return extendedpo2_customer;
    }

    public void setExtendedpo2_customer(extendedPO2_Customer extendedpo2_customer) {
        this.extendedpo2_customer = extendedpo2_customer;
    }
    public extendedPO2_PurchaseOrder getExtendedpo2_purchaseorder() {
        return extendedpo2_purchaseorder;
    }

    public void setExtendedpo2_purchaseorder(extendedPO2_PurchaseOrder extendedpo2_purchaseorder) {
        this.extendedpo2_purchaseorder = extendedpo2_purchaseorder;
    }
    public extendedPO2_Item getExtendedpo2_item() {
        return extendedpo2_item;
    }

    public void setExtendedpo2_item(extendedPO2_Item extendedpo2_item) {
        this.extendedpo2_item = extendedpo2_item;
    }
    public extendedPO2_Address getExtendedpo2_address() {
        return extendedpo2_address;
    }

    public void setExtendedpo2_address(extendedPO2_Address extendedpo2_address) {
        this.extendedpo2_address = extendedpo2_address;
    }
    public extendedPO2_Customer getExtendedpo2_customer() {
        return extendedpo2_customer;
    }

    public void setExtendedpo2_customer(extendedPO2_Customer extendedpo2_customer) {
        this.extendedpo2_customer = extendedpo2_customer;
    }
    public extendedPO2_Address getExtendedpo2_address() {
        return extendedpo2_address;
    }

    public void setExtendedpo2_address(extendedPO2_Address extendedpo2_address) {
        this.extendedpo2_address = extendedpo2_address;
    }
    public List<extendedPO2_Item> getExtendedpo2_items() {
        return extendedpo2_items;
    }

    public void addExtendedpo2_item(Extendedpo2_item extendedpo2_item) {
        this.extendedpo2_items.add(extendedpo2_item);
    }

}