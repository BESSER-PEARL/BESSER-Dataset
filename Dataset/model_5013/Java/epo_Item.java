





import java.util.List;
import java.util.ArrayList;

public class epo_Item  {

    private String partNum;
    private int quantity;
    private String shipDate;
    private String productName;
    private int USPrice;
    private String comment;



    public epo_Item(
        String partNum,        int quantity,        String shipDate,        String productName,        int USPrice,        String comment    ) {
        this.partNum = partNum;
        this.quantity = quantity;
        this.shipDate = shipDate;
        this.productName = productName;
        this.USPrice = USPrice;
        this.comment = comment;
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
    public String getShipdate() {
        return shipDate;
    }

    public void setShipdate(String shipDate) {
        this.shipDate = shipDate;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public int getUsprice() {
        return USPrice;
    }

    public void setUsprice(int USPrice) {
        this.USPrice = USPrice;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}