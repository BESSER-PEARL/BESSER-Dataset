





import java.util.List;
import java.util.ArrayList;

public class esof_homework4_q2_Item  {

    private String shipDate;
    private String comment;
    private int USPrice;
    private String productName;
    private int quantity;
    private String partNum;





    private esof_homework4_q2_PurchaseOrder esof_homework4_q2_purchaseorder;


    public esof_homework4_q2_Item(
        String shipDate,        String comment,        int USPrice,        String productName,        int quantity,        String partNum    ) {
        this.shipDate = shipDate;
        this.comment = comment;
        this.USPrice = USPrice;
        this.productName = productName;
        this.quantity = quantity;
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
    public String getPartnum() {
        return partNum;
    }

    public void setPartnum(String partNum) {
        this.partNum = partNum;
    }

    public esof_homework4_q2_PurchaseOrder getEsof_homework4_q2_purchaseorder() {
        return esof_homework4_q2_purchaseorder;
    }

    public void setEsof_homework4_q2_purchaseorder(esof_homework4_q2_PurchaseOrder esof_homework4_q2_purchaseorder) {
        this.esof_homework4_q2_purchaseorder = esof_homework4_q2_purchaseorder;
    }

}