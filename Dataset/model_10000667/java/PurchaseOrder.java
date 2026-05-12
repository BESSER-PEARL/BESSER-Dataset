




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class PurchaseOrder  {

    private LocalDate Date;
    private int PurchaseOrderID;
    private float Quantity;
    private int ItemID;
    private float Price;
    private int VendorID;





    private List<Items> itemss;


    public PurchaseOrder(
        LocalDate Date,        int PurchaseOrderID,        float Quantity,        int ItemID,        float Price,        int VendorID    ) {
        this.Date = Date;
        this.PurchaseOrderID = PurchaseOrderID;
        this.Quantity = Quantity;
        this.ItemID = ItemID;
        this.Price = Price;
        this.VendorID = VendorID;
        this.itemss = new ArrayList<>();
    }

    public PurchaseOrder(
        LocalDate Date,        int PurchaseOrderID,        float Quantity,        int ItemID,        float Price,        int VendorID        ArrayList<Items> itemss    ) {
        this.Date = Date;
        this.PurchaseOrderID = PurchaseOrderID;
        this.Quantity = Quantity;
        this.ItemID = ItemID;
        this.Price = Price;
        this.VendorID = VendorID;
        this.itemss = itemss;
    }

    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public int getPurchaseorderid() {
        return PurchaseOrderID;
    }

    public void setPurchaseorderid(int PurchaseOrderID) {
        this.PurchaseOrderID = PurchaseOrderID;
    }
    public float getQuantity() {
        return Quantity;
    }

    public void setQuantity(float Quantity) {
        this.Quantity = Quantity;
    }
    public int getItemid() {
        return ItemID;
    }

    public void setItemid(int ItemID) {
        this.ItemID = ItemID;
    }
    public float getPrice() {
        return Price;
    }

    public void setPrice(float Price) {
        this.Price = Price;
    }
    public int getVendorid() {
        return VendorID;
    }

    public void setVendorid(int VendorID) {
        this.VendorID = VendorID;
    }

    public List<Items> getItemss() {
        return itemss;
    }

    public void addItems(Items items) {
        this.itemss.add(items);
    }

}