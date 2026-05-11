





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_ServiceResourceFilter extends ResourceFilter {

    private String serviceURL;
    private boolean everyService;



    public camel_organisation_ServiceResourceFilter(
        String serviceURL,        boolean everyService    ) {
        super(
        );
        this.serviceURL = serviceURL;
        this.everyService = everyService;
    }


    public String getServiceurl() {
        return serviceURL;
    }

    public void setServiceurl(String serviceURL) {
        this.serviceURL = serviceURL;
    }
    public boolean getEveryservice() {
        return everyService;
    }

    public void setEveryservice(boolean everyService) {
        this.everyService = everyService;
    }


}