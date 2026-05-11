





import java.util.List;
import java.util.ArrayList;

public class epo2_PurchaseOrder  {

    private String orderDate;
    private String comment;
    private int totalAmount;
    private String status;





    private epo2_PurchaseOrder epo2_purchaseorder;




    private epo2_Address epo2_address;




    private epo2_Address epo2_address;


    public epo2_PurchaseOrder(
        String orderDate,        String comment,        int totalAmount,        String status    ) {
        this.orderDate = orderDate;
        this.comment = comment;
        this.totalAmount = totalAmount;
        this.status = status;
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

    public epo2_PurchaseOrder getEpo2_purchaseorder() {
        return epo2_purchaseorder;
    }

    public void setEpo2_purchaseorder(epo2_PurchaseOrder epo2_purchaseorder) {
        this.epo2_purchaseorder = epo2_purchaseorder;
    }
    public epo2_Address getEpo2_address() {
        return epo2_address;
    }

    public void setEpo2_address(epo2_Address epo2_address) {
        this.epo2_address = epo2_address;
    }
    public epo2_Address getEpo2_address() {
        return epo2_address;
    }

    public void setEpo2_address(epo2_Address epo2_address) {
        this.epo2_address = epo2_address;
    }

}