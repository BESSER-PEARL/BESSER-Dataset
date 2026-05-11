





import java.util.List;
import java.util.ArrayList;

public class epo2_Item  {

    private String shipDate;
    private String comment;
    private int quantity;
    private String partNum;
    private String productName;
    private int USPrice;



    public epo2_Item(
        String shipDate,        String comment,        int quantity,        String partNum,        String productName,        int USPrice    ) {
        this.shipDate = shipDate;
        this.comment = comment;
        this.quantity = quantity;
        this.partNum = partNum;
        this.productName = productName;
        this.USPrice = USPrice;
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
    public int getUsprice() {
        return USPrice;
    }

    public void setUsprice(int USPrice) {
        this.USPrice = USPrice;
    }


}