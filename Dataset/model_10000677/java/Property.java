





import java.util.List;
import java.util.ArrayList;

public class Property  {

    private String location;
    private String property_type;
    private String property_id;
    private String address;





    private Payment payment;




    private List<Management> managements;




    private Buyer buyer;




    private Seller seller;


    public Property(
        String location,        String property_type,        String property_id,        String address    ) {
        this.location = location;
        this.property_type = property_type;
        this.property_id = property_id;
        this.address = address;
        this.managements = new ArrayList<>();
    }

    public Property(
        String location,        String property_type,        String property_id,        String address        ArrayList<Management> managements    ) {
        this.location = location;
        this.property_type = property_type;
        this.property_id = property_id;
        this.address = address;
        this.managements = managements;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getProperty_type() {
        return property_type;
    }

    public void setProperty_type(String property_type) {
        this.property_type = property_type;
    }
    public String getProperty_id() {
        return property_id;
    }

    public void setProperty_id(String property_id) {
        this.property_id = property_id;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public List<Management> getManagements() {
        return managements;
    }

    public void addManagement(Management management) {
        this.managements.add(management);
    }
    public Buyer getBuyer() {
        return buyer;
    }

    public void setBuyer(Buyer buyer) {
        this.buyer = buyer;
    }
    public Seller getSeller() {
        return seller;
    }

    public void setSeller(Seller seller) {
        this.seller = seller;
    }

}