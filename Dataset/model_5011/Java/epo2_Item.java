





import java.util.List;
import java.util.ArrayList;

public class epo2_Item  {

    private String productName;
    private String partNum;
    private String shipDate;
    private String comment;
    private int quantity;
    private int USPrice;





    private epo2_PurchaseOrder epo2_purchaseorder;




    private epo2_PurchaseOrder epo2_purchaseorder;


    public epo2_Item(
        String productName,        String partNum,        String shipDate,        String comment,        int quantity,        int USPrice    ) {
        this.productName = productName;
        this.partNum = partNum;
        this.shipDate = shipDate;
        this.comment = comment;
        this.quantity = quantity;
        this.USPrice = USPrice;
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
    public int getUsprice() {
        return USPrice;
    }

    public void setUsprice(int USPrice) {
        this.USPrice = USPrice;
    }

    public epo2_PurchaseOrder getEpo2_purchaseorder() {
        return epo2_purchaseorder;
    }

    public void setEpo2_purchaseorder(epo2_PurchaseOrder epo2_purchaseorder) {
        this.epo2_purchaseorder = epo2_purchaseorder;
    }
    public epo2_PurchaseOrder getEpo2_purchaseorder() {
        return epo2_purchaseorder;
    }

    public void setEpo2_purchaseorder(epo2_PurchaseOrder epo2_purchaseorder) {
        this.epo2_purchaseorder = epo2_purchaseorder;
    }

}