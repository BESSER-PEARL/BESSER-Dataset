





import java.util.List;
import java.util.ArrayList;

public class extendedPO2_Item  {

    private String productName;
    private String partNum;
    private int USPrice;
    private int quantity;
    private String comment;
    private String shipDate;



    public extendedPO2_Item(
        String productName,        String partNum,        int USPrice,        int quantity,        String comment,        String shipDate    ) {
        this.productName = productName;
        this.partNum = partNum;
        this.USPrice = USPrice;
        this.quantity = quantity;
        this.comment = comment;
        this.shipDate = shipDate;
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
    public int getUsprice() {
        return USPrice;
    }

    public void setUsprice(int USPrice) {
        this.USPrice = USPrice;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
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


}