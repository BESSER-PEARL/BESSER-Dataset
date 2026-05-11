





import java.util.List;
import java.util.ArrayList;

public class epo2_PurchaseOrder  {

    private String orderDate;
    private String status;
    private int totalAmount;
    private String comment;





    private epo2_PurchaseOrder epo2_purchaseorder;


    public epo2_PurchaseOrder(
        String orderDate,        String status,        int totalAmount,        String comment    ) {
        this.orderDate = orderDate;
        this.status = status;
        this.totalAmount = totalAmount;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public epo2_PurchaseOrder getEpo2_purchaseorder() {
        return epo2_purchaseorder;
    }

    public void setEpo2_purchaseorder(epo2_PurchaseOrder epo2_purchaseorder) {
        this.epo2_purchaseorder = epo2_purchaseorder;
    }

}