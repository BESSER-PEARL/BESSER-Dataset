





import java.util.List;
import java.util.ArrayList;

public class services_RFSService extends Service {

    private String functionalCategory;
    private String location;



    public services_RFSService(
        String functionalCategory,        String location    ) {
        super(
        );
        this.functionalCategory = functionalCategory;
        this.location = location;
    }


    public String getFunctionalcategory() {
        return functionalCategory;
    }

    public void setFunctionalcategory(String functionalCategory) {
        this.functionalCategory = functionalCategory;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}