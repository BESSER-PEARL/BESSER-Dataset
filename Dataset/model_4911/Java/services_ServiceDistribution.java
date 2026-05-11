





import java.util.List;
import java.util.ArrayList;

public class services_ServiceDistribution extends Base {






    private services_Service services_service;




    private List<services_Expression> services_expressions;




    private List<services_DistributionEntry> services_distributionentrys;


    public services_ServiceDistribution(
    ) {
        super(
        );
        this.services_expressions = new ArrayList<>();
        this.services_distributionentrys = new ArrayList<>();
    }

    public services_ServiceDistribution(
        ArrayList<services_Expression> services_expressions,        ArrayList<services_DistributionEntry> services_distributionentrys    ) {
        this.services_expressions = services_expressions;
        this.services_distributionentrys = services_distributionentrys;
    }


    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }
    public List<services_Expression> getServices_expressions() {
        return services_expressions;
    }

    public void addServices_expression(Services_expression services_expression) {
        this.services_expressions.add(services_expression);
    }
    public List<services_DistributionEntry> getServices_distributionentrys() {
        return services_distributionentrys;
    }

    public void addServices_distributionentry(Services_distributionentry services_distributionentry) {
        this.services_distributionentrys.add(services_distributionentry);
    }

}