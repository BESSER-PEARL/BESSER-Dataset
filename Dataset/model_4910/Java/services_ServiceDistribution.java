





import java.util.List;
import java.util.ArrayList;

public class services_ServiceDistribution extends Base {






    private List<services_DistributionEntry> services_distributionentrys;




    private services_Service services_service;


    public services_ServiceDistribution(
    ) {
        super(
        );
        this.services_distributionentrys = new ArrayList<>();
    }

    public services_ServiceDistribution(
        ArrayList<services_DistributionEntry> services_distributionentrys    ) {
        this.services_distributionentrys = services_distributionentrys;
    }


    public List<services_DistributionEntry> getServices_distributionentrys() {
        return services_distributionentrys;
    }

    public void addServices_distributionentry(Services_distributionentry services_distributionentry) {
        this.services_distributionentrys.add(services_distributionentry);
    }
    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}