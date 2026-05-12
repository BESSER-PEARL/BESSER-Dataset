





import java.util.List;
import java.util.ArrayList;

public class Supplier  {

    private int contact_no;
    private String email;
    private String Supplier_id;
    private String address;
    private String name;



    public Supplier(
        int contact_no,        String email,        String Supplier_id,        String address,        String name    ) {
        this.contact_no = contact_no;
        this.email = email;
        this.Supplier_id = Supplier_id;
        this.address = address;
        this.name = name;
    }


    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getSupplier_id() {
        return Supplier_id;
    }

    public void setSupplier_id(String Supplier_id) {
        this.Supplier_id = Supplier_id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}