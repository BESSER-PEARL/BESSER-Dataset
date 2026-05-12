





import java.util.List;
import java.util.ArrayList;

public class Supplier  {

    private String Supplier_id;
    private int contact_no;
    private String email;
    private String address;
    private String name;





    private Orders orders;


    public Supplier(
        String Supplier_id,        int contact_no,        String email,        String address,        String name    ) {
        this.Supplier_id = Supplier_id;
        this.contact_no = contact_no;
        this.email = email;
        this.address = address;
        this.name = name;
    }


    public String getSupplier_id() {
        return Supplier_id;
    }

    public void setSupplier_id(String Supplier_id) {
        this.Supplier_id = Supplier_id;
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

    public Orders getOrders() {
        return orders;
    }

    public void setOrders(Orders orders) {
        this.orders = orders;
    }

}