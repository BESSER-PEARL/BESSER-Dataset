





import java.util.List;
import java.util.ArrayList;

public class Vendor  {

    private int ItemID;
    private int VendorID;
    private String Address;





    private List<PurchaseOrder> purchaseorders;


    public Vendor(
        int ItemID,        int VendorID,        String Address    ) {
        this.ItemID = ItemID;
        this.VendorID = VendorID;
        this.Address = Address;
        this.purchaseorders = new ArrayList<>();
    }

    public Vendor(
        int ItemID,        int VendorID,        String Address        ArrayList<PurchaseOrder> purchaseorders    ) {
        this.ItemID = ItemID;
        this.VendorID = VendorID;
        this.Address = Address;
        this.purchaseorders = purchaseorders;
    }

    public int getItemid() {
        return ItemID;
    }

    public void setItemid(int ItemID) {
        this.ItemID = ItemID;
    }
    public int getVendorid() {
        return VendorID;
    }

    public void setVendorid(int VendorID) {
        this.VendorID = VendorID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public List<PurchaseOrder> getPurchaseorders() {
        return purchaseorders;
    }

    public void addPurchaseorder(Purchaseorder purchaseorder) {
        this.purchaseorders.add(purchaseorder);
    }

}