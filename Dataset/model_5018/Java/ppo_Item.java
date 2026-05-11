





import java.util.List;
import java.util.ArrayList;

public class ppo_Item  {

    private String partNum;
    private int uSPrice;
    private String comment;
    private String productName;
    private int quantity;
    private String shipDate;



    public ppo_Item(
        String partNum,        int uSPrice,        String comment,        String productName,        int quantity,        String shipDate    ) {
        this.partNum = partNum;
        this.uSPrice = uSPrice;
        this.comment = comment;
        this.productName = productName;
        this.quantity = quantity;
        this.shipDate = shipDate;
    }


    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
    }
    public int getUsprice() {
        return uSPrice;
    }

    public void setUsprice(int uSPrice) {
        this.uSPrice = uSPrice;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
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


}