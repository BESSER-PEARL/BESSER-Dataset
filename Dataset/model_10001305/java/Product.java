





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int VendorID;
    private int InventoryMinQuantity;
    private String Description;
    private int InventoryQuantity;
    private int ProductID;



    public Product(
        int VendorID,        int InventoryMinQuantity,        String Description,        int InventoryQuantity,        int ProductID    ) {
        this.VendorID = VendorID;
        this.InventoryMinQuantity = InventoryMinQuantity;
        this.Description = Description;
        this.InventoryQuantity = InventoryQuantity;
        this.ProductID = ProductID;
    }


    public int getVendorid() {
        return VendorID;
    }

    public void setVendorid(int VendorID) {
        this.VendorID = VendorID;
    }
    public int getInventoryminquantity() {
        return InventoryMinQuantity;
    }

    public void setInventoryminquantity(int InventoryMinQuantity) {
        this.InventoryMinQuantity = InventoryMinQuantity;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public int getInventoryquantity() {
        return InventoryQuantity;
    }

    public void setInventoryquantity(int InventoryQuantity) {
        this.InventoryQuantity = InventoryQuantity;
    }
    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }


}