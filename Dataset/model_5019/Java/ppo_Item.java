





import java.util.List;
import java.util.ArrayList;

public class ppo_Item  {

    private int quantity;
    private int USPrice;
    private String productName;
    private String shipDate;
    private String comment;
    private String partNum;





    private ppo_PurchaseOrder ppo_purchaseorder;


    public ppo_Item(
        int quantity,        int USPrice,        String productName,        String shipDate,        String comment,        String partNum    ) {
        this.quantity = quantity;
        this.USPrice = USPrice;
        this.productName = productName;
        this.shipDate = shipDate;
        this.comment = comment;
        this.partNum = partNum;
    }


    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public int getUsprice() {
        return USPrice;
    }

    public void setUsprice(int USPrice) {
        this.USPrice = USPrice;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public String getShipdate() {
        return shipDate;
    }

    public void setShipdate(String shipDate) {
        this.shipDate = shipDate;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
    }

    public ppo_PurchaseOrder getPpo_purchaseorder() {
        return ppo_purchaseorder;
    }

    public void setPpo_purchaseorder(ppo_PurchaseOrder ppo_purchaseorder) {
        this.ppo_purchaseorder = ppo_purchaseorder;
    }

}