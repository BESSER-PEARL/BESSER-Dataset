





import java.util.List;
import java.util.ArrayList;

public class services_DistributionEntry extends Base {

    private String resourceOrigin;



    public services_DistributionEntry(
        String resourceOrigin    ) {
        super(
        );
        this.resourceOrigin = resourceOrigin;
    }


    public String getResourceorigin() {
        return resourceOrigin;
    }

    public void setResourceorigin(String resourceOrigin) {
        this.resourceOrigin = resourceOrigin;
    }


}