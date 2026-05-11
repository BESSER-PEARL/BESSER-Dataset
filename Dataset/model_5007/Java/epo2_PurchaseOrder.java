




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class epo2_PurchaseOrder  {

    private int totalAmount;
    private String status;
    private LocalDate orderDate;
    private String comment;





    private epo2_Address epo2_address;




    private epo2_Supplier epo2_supplier;




    private epo2_Supplier epo2_supplier;




    private epo2_Customer epo2_customer;




    private List<epo2_Item> epo2_items;




    private epo2_Address epo2_address;




    private epo2_Customer epo2_customer;




    private epo2_PurchaseOrder epo2_purchaseorder;




    private epo2_Supplier epo2_supplier;




    private epo2_Item epo2_item;


    public epo2_PurchaseOrder(
        int totalAmount,        String status,        LocalDate orderDate,        String comment    ) {
        this.totalAmount = totalAmount;
        this.status = status;
        this.orderDate = orderDate;
        this.comment = comment;
        this.epo2_items = new ArrayList<>();
    }

    public epo2_PurchaseOrder(
        int totalAmount,        String status,        LocalDate orderDate,        String comment        ArrayList<epo2_Item> epo2_items    ) {
        this.totalAmount = totalAmount;
        this.status = status;
        this.orderDate = orderDate;
        this.comment = comment;
        this.epo2_items = epo2_items;
    }

    public int getTotalamount() {
        return totalAmount;
    }

    public void setTotalamount(int totalAmount) {
        this.totalAmount = totalAmount;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public LocalDate getOrderdate() {
        return orderDate;
    }

    public void setOrderdate(LocalDate orderDate) {
        this.orderDate = orderDate;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public epo2_Address getEpo2_address() {
        return epo2_address;
    }

    public void setEpo2_address(epo2_Address epo2_address) {
        this.epo2_address = epo2_address;
    }
    public epo2_Supplier getEpo2_supplier() {
        return epo2_supplier;
    }

    public void setEpo2_supplier(epo2_Supplier epo2_supplier) {
        this.epo2_supplier = epo2_supplier;
    }
    public epo2_Supplier getEpo2_supplier() {
        return epo2_supplier;
    }

    public void setEpo2_supplier(epo2_Supplier epo2_supplier) {
        this.epo2_supplier = epo2_supplier;
    }
    public epo2_Customer getEpo2_customer() {
        return epo2_customer;
    }

    public void setEpo2_customer(epo2_Customer epo2_customer) {
        this.epo2_customer = epo2_customer;
    }
    public List<epo2_Item> getEpo2_items() {
        return epo2_items;
    }

    public void addEpo2_item(Epo2_item epo2_item) {
        this.epo2_items.add(epo2_item);
    }
    public epo2_Address getEpo2_address() {
        return epo2_address;
    }

    public void setEpo2_address(epo2_Address epo2_address) {
        this.epo2_address = epo2_address;
    }
    public epo2_Customer getEpo2_customer() {
        return epo2_customer;
    }

    public void setEpo2_customer(epo2_Customer epo2_customer) {
        this.epo2_customer = epo2_customer;
    }
    public epo2_PurchaseOrder getEpo2_purchaseorder() {
        return epo2_purchaseorder;
    }

    public void setEpo2_purchaseorder(epo2_PurchaseOrder epo2_purchaseorder) {
        this.epo2_purchaseorder = epo2_purchaseorder;
    }
    public epo2_Supplier getEpo2_supplier() {
        return epo2_supplier;
    }

    public void setEpo2_supplier(epo2_Supplier epo2_supplier) {
        this.epo2_supplier = epo2_supplier;
    }
    public epo2_Item getEpo2_item() {
        return epo2_item;
    }

    public void setEpo2_item(epo2_Item epo2_item) {
        this.epo2_item = epo2_item;
    }

}