





import java.util.List;
import java.util.ArrayList;

public class services_DistributionEntry extends Base {

    private String resourceOrigin;





    private services_ServiceDistribution services_servicedistribution;


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

    public services_ServiceDistribution getServices_servicedistribution() {
        return services_servicedistribution;
    }

    public void setServices_servicedistribution(services_ServiceDistribution services_servicedistribution) {
        this.services_servicedistribution = services_servicedistribution;
    }

}