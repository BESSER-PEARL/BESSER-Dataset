





import java.util.List;
import java.util.ArrayList;

public class epo_PurchaseOrder  {

    private int totalAmount;
    private String orderDate;
    private String comment;
    private String status;





    private epo_Supplier epo_supplier;




    private epo_Customer epo_customer;




    private epo_Address epo_address;




    private epo_PurchaseOrder epo_purchaseorder;




    private epo_Address epo_address;




    private List<epo_Item> epo_items;




    private epo_Supplier epo_supplier;




    private epo_Supplier epo_supplier;




    private epo_Customer epo_customer;




    private epo_Item epo_item;


    public epo_PurchaseOrder(
        int totalAmount,        String orderDate,        String comment,        String status    ) {
        this.totalAmount = totalAmount;
        this.orderDate = orderDate;
        this.comment = comment;
        this.status = status;
        this.epo_items = new ArrayList<>();
    }

    public epo_PurchaseOrder(
        int totalAmount,        String orderDate,        String comment,        String status        ArrayList<epo_Item> epo_items    ) {
        this.totalAmount = totalAmount;
        this.orderDate = orderDate;
        this.comment = comment;
        this.status = status;
        this.epo_items = epo_items;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public epo_Supplier getEpo_supplier() {
        return epo_supplier;
    }

    public void setEpo_supplier(epo_Supplier epo_supplier) {
        this.epo_supplier = epo_supplier;
    }
    public epo_Customer getEpo_customer() {
        return epo_customer;
    }

    public void setEpo_customer(epo_Customer epo_customer) {
        this.epo_customer = epo_customer;
    }
    public epo_Address getEpo_address() {
        return epo_address;
    }

    public void setEpo_address(epo_Address epo_address) {
        this.epo_address = epo_address;
    }
    public epo_PurchaseOrder getEpo_purchaseorder() {
        return epo_purchaseorder;
    }

    public void setEpo_purchaseorder(epo_PurchaseOrder epo_purchaseorder) {
        this.epo_purchaseorder = epo_purchaseorder;
    }
    public epo_Address getEpo_address() {
        return epo_address;
    }

    public void setEpo_address(epo_Address epo_address) {
        this.epo_address = epo_address;
    }
    public List<epo_Item> getEpo_items() {
        return epo_items;
    }

    public void addEpo_item(Epo_item epo_item) {
        this.epo_items.add(epo_item);
    }
    public epo_Supplier getEpo_supplier() {
        return epo_supplier;
    }

    public void setEpo_supplier(epo_Supplier epo_supplier) {
        this.epo_supplier = epo_supplier;
    }
    public epo_Supplier getEpo_supplier() {
        return epo_supplier;
    }

    public void setEpo_supplier(epo_Supplier epo_supplier) {
        this.epo_supplier = epo_supplier;
    }
    public epo_Customer getEpo_customer() {
        return epo_customer;
    }

    public void setEpo_customer(epo_Customer epo_customer) {
        this.epo_customer = epo_customer;
    }
    public epo_Item getEpo_item() {
        return epo_item;
    }

    public void setEpo_item(epo_Item epo_item) {
        this.epo_item = epo_item;
    }

}