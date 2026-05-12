





import java.util.List;
import java.util.ArrayList;

public class Vendor  {

    private int Contact_Number;
    private int VendorID;
    private String Name;
    private String Email;
    private String Address;





    private List<Product> products;


    public Vendor(
        int Contact_Number,        int VendorID,        String Name,        String Email,        String Address    ) {
        this.Contact_Number = Contact_Number;
        this.VendorID = VendorID;
        this.Name = Name;
        this.Email = Email;
        this.Address = Address;
        this.products = new ArrayList<>();
    }

    public Vendor(
        int Contact_Number,        int VendorID,        String Name,        String Email,        String Address        ArrayList<Product> products    ) {
        this.Contact_Number = Contact_Number;
        this.VendorID = VendorID;
        this.Name = Name;
        this.Email = Email;
        this.Address = Address;
        this.products = products;
    }

    public int getContact_number() {
        return Contact_Number;
    }

    public void setContact_number(int Contact_Number) {
        this.Contact_Number = Contact_Number;
    }
    public int getVendorid() {
        return VendorID;
    }

    public void setVendorid(int VendorID) {
        this.VendorID = VendorID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}