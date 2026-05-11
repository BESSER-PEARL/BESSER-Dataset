





import java.util.List;
import java.util.ArrayList;

public class services_RFSService extends Service {

    private String functionalCategory;



    public services_RFSService(
        String functionalCategory    ) {
        super(
        );
        this.functionalCategory = functionalCategory;
    }


    public String getFunctionalcategory() {
        return functionalCategory;
    }

    public void setFunctionalcategory(String functionalCategory) {
        this.functionalCategory = functionalCategory;
    }


}