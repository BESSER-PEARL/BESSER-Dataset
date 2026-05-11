




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class epo2_Item  {

    private int usPrice;
    private String comment;
    private int quantity;
    private String partNum;
    private String productName;
    private LocalDate shipDate;



    public epo2_Item(
        int usPrice,        String comment,        int quantity,        String partNum,        String productName,        LocalDate shipDate    ) {
        this.usPrice = usPrice;
        this.comment = comment;
        this.quantity = quantity;
        this.partNum = partNum;
        this.productName = productName;
        this.shipDate = shipDate;
    }


    public int getUsprice() {
        return usPrice;
    }

    public void setUsprice(int usPrice) {
        this.usPrice = usPrice;
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
    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public LocalDate getShipdate() {
        return shipDate;
    }

    public void setShipdate(LocalDate shipDate) {
        this.shipDate = shipDate;
    }


}