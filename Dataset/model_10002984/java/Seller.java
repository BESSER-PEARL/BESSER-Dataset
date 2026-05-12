





import java.util.List;
import java.util.ArrayList;

public class Seller  {

    private String seller_id;
    private String property_id;





    private List<Property> propertys;


    public Seller(
        String seller_id,        String property_id    ) {
        this.seller_id = seller_id;
        this.property_id = property_id;
        this.propertys = new ArrayList<>();
    }

    public Seller(
        String seller_id,        String property_id        ArrayList<Property> propertys    ) {
        this.seller_id = seller_id;
        this.property_id = property_id;
        this.propertys = propertys;
    }

    public String getSeller_id() {
        return seller_id;
    }

    public void setSeller_id(String seller_id) {
        this.seller_id = seller_id;
    }
    public String getProperty_id() {
        return property_id;
    }

    public void setProperty_id(String property_id) {
        this.property_id = property_id;
    }

    public List<Property> getPropertys() {
        return propertys;
    }

    public void addProperty(Property property) {
        this.propertys.add(property);
    }

}