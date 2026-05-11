





import java.util.List;
import java.util.ArrayList;

public class services_DerivedResource extends BaseResource {






    private services_DistributionEntry services_distributionentry;




    private services_ServiceProfile services_serviceprofile;


    public services_DerivedResource(
    ) {
        super(
        );
    }



    public services_DistributionEntry getServices_distributionentry() {
        return services_distributionentry;
    }

    public void setServices_distributionentry(services_DistributionEntry services_distributionentry) {
        this.services_distributionentry = services_distributionentry;
    }
    public services_ServiceProfile getServices_serviceprofile() {
        return services_serviceprofile;
    }

    public void setServices_serviceprofile(services_ServiceProfile services_serviceprofile) {
        this.services_serviceprofile = services_serviceprofile;
    }

}