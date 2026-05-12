





import java.util.List;
import java.util.ArrayList;

public class Owner  {

    private String owner_id;
    private String property_id;





    private List<Property> propertys;


    public Owner(
        String owner_id,        String property_id    ) {
        this.owner_id = owner_id;
        this.property_id = property_id;
        this.propertys = new ArrayList<>();
    }

    public Owner(
        String owner_id,        String property_id        ArrayList<Property> propertys    ) {
        this.owner_id = owner_id;
        this.property_id = property_id;
        this.propertys = propertys;
    }

    public String getOwner_id() {
        return owner_id;
    }

    public void setOwner_id(String owner_id) {
        this.owner_id = owner_id;
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