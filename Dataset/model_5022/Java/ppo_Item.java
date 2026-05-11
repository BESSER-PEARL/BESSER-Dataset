





import java.util.List;
import java.util.ArrayList;

public class ppo_Item  {

    private String productName;
    private String comment;
    private int quantity;
    private int USPrice;
    private String shipDate;
    private String partNum;





    private ppo_PurchaseOrder ppo_purchaseorder;


    public ppo_Item(
        String productName,        String comment,        int quantity,        int USPrice,        String shipDate,        String partNum    ) {
        this.productName = productName;
        this.comment = comment;
        this.quantity = quantity;
        this.USPrice = USPrice;
        this.shipDate = shipDate;
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
    public int getUsprice() {
        return USPrice;
    }

    public void setUsprice(int USPrice) {
        this.USPrice = USPrice;
    }
    public String getShipdate() {
        return shipDate;
    }

    public void setShipdate(String shipDate) {
        this.shipDate = shipDate;
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