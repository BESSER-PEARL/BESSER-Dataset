





import java.util.List;
import java.util.ArrayList;

public class purchaseOrder_Item  {

    private String productName;
    private String comment;
    private int quantity;
    private String shipDate;
    private int USPrice;
    private String partNum;





    private purchaseOrder_PurchaseOrder purchaseorder_purchaseorder;


    public purchaseOrder_Item(
        String productName,        String comment,        int quantity,        String shipDate,        int USPrice,        String partNum    ) {
        this.productName = productName;
        this.comment = comment;
        this.quantity = quantity;
        this.shipDate = shipDate;
        this.USPrice = USPrice;
        this.partNum = partNum;
    }


    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getShipdate() {
        return shipDate;
    }

    public void setShipdate(String shipDate) {
        this.shipDate = shipDate;
    }
    public int getUsprice() {
        return USPrice;
    }

    public void setUsprice(int USPrice) {
        this.USPrice = USPrice;
    }
    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
    }

    public purchaseOrder_PurchaseOrder getPurchaseorder_purchaseorder() {
        return purchaseorder_purchaseorder;
    }

    public void setPurchaseorder_purchaseorder(purchaseOrder_PurchaseOrder purchaseorder_purchaseorder) {
        this.purchaseorder_purchaseorder = purchaseorder_purchaseorder;
    }

}