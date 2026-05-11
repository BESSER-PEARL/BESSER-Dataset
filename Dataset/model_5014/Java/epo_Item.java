





import java.util.List;
import java.util.ArrayList;

public class epo_Item  {

    private int quantity;
    private int USPrice;
    private String comment;
    private String partNum;
    private String shipDate;
    private String productName;



    public epo_Item(
        int quantity,        int USPrice,        String comment,        String partNum,        String shipDate,        String productName    ) {
        this.quantity = quantity;
        this.USPrice = USPrice;
        this.comment = comment;
        this.partNum = partNum;
        this.shipDate = shipDate;
        this.productName = productName;
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


}