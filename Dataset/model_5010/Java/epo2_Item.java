





import java.util.List;
import java.util.ArrayList;

public class epo2_Item  {

    private String partNum;
    private int USPrice;
    private String productName;
    private int quantity;
    private String shipDate;
    private String comment;



    public epo2_Item(
        String partNum,        int USPrice,        String productName,        int quantity,        String shipDate,        String comment    ) {
        this.partNum = partNum;
        this.USPrice = USPrice;
        this.productName = productName;
        this.quantity = quantity;
        this.shipDate = shipDate;
        this.comment = comment;
    }


    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }


}