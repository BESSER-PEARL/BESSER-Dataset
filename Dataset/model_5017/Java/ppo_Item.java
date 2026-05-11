




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ppo_Item  {

    private int uSPrice;
    private LocalDate shipDate;
    private String comment;
    private String productName;
    private String partNum;
    private int quantity;



    public ppo_Item(
        int uSPrice,        LocalDate shipDate,        String comment,        String productName,        String partNum,        int quantity    ) {
        this.uSPrice = uSPrice;
        this.shipDate = shipDate;
        this.comment = comment;
        this.productName = productName;
        this.partNum = partNum;
        this.quantity = quantity;
    }


    public int getUsprice() {
        return uSPrice;
    }

    public void setUsprice(int uSPrice) {
        this.uSPrice = uSPrice;
    }
    public LocalDate getShipdate() {
        return shipDate;
    }

    public void setShipdate(LocalDate shipDate) {
        this.shipDate = shipDate;
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
    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}