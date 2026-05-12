





import java.util.List;
import java.util.ArrayList;

public class Property1  {

    private String location;
    private String property_id;
    private String address;
    private String property_type;



    public Property1(
        String location,        String property_id,        String address,        String property_type    ) {
        this.location = location;
        this.property_id = property_id;
        this.address = address;
        this.property_type = property_type;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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
    public String getProperty_type() {
        return property_type;
    }

    public void setProperty_type(String property_type) {
        this.property_type = property_type;
    }


}