





import java.util.List;
import java.util.ArrayList;

public class Property  {

    private String address;
    private String location;
    private String property_type;
    private String property_id;



    public Property(
        String address,        String location,        String property_type,        String property_id    ) {
        this.address = address;
        this.location = location;
        this.property_type = property_type;
        this.property_id = property_id;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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


}