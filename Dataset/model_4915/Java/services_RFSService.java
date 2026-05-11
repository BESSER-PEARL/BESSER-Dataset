





import java.util.List;
import java.util.ArrayList;

public class services_RFSService extends Service {

    private String location;
    private String functionalCategory;



    public services_RFSService(
        String location,        String functionalCategory    ) {
        super(
        );
        this.location = location;
        this.functionalCategory = functionalCategory;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getFunctionalcategory() {
        return functionalCategory;
    }

    public void setFunctionalcategory(String functionalCategory) {
        this.functionalCategory = functionalCategory;
    }


}