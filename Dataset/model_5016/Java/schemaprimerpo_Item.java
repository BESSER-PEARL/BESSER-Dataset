





import java.util.List;
import java.util.ArrayList;

public class schemaprimerpo_Item  {

    private String quantity;
    private String comment;
    private String shipDate;
    private String uSPrice;
    private String productName;
    private String partNum;





    private schemaprimerpo_PurchaseOrder schemaprimerpo_purchaseorder;


    public schemaprimerpo_Item(
        String quantity,        String comment,        String shipDate,        String uSPrice,        String productName,        String partNum    ) {
        this.quantity = quantity;
        this.comment = comment;
        this.shipDate = shipDate;
        this.uSPrice = uSPrice;
        this.productName = productName;
        this.partNum = partNum;
    }


    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getShipdate() {
        return shipDate;
    }

    public void setShipdate(String shipDate) {
        this.shipDate = shipDate;
    }
    public String getUsprice() {
        return uSPrice;
    }

    public void setUsprice(String uSPrice) {
        this.uSPrice = uSPrice;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
    }

    public schemaprimerpo_PurchaseOrder getSchemaprimerpo_purchaseorder() {
        return schemaprimerpo_purchaseorder;
    }

    public void setSchemaprimerpo_purchaseorder(schemaprimerpo_PurchaseOrder schemaprimerpo_purchaseorder) {
        this.schemaprimerpo_purchaseorder = schemaprimerpo_purchaseorder;
    }

}