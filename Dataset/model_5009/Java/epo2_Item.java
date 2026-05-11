





import java.util.List;
import java.util.ArrayList;

public class epo2_Item  {

    private String comment;
    private int USPrice;
    private String partNum;
    private String shipDate;
    private String productName;
    private int quantity;



    public epo2_Item(
        String comment,        int USPrice,        String partNum,        String shipDate,        String productName,        int quantity    ) {
        this.comment = comment;
        this.USPrice = USPrice;
        this.partNum = partNum;
        this.shipDate = shipDate;
        this.productName = productName;
        this.quantity = quantity;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
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
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }


}