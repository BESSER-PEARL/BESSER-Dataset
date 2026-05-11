





import java.util.List;
import java.util.ArrayList;

public class services_ServiceDistribution  {






    private List<services_Expression> services_expressions;




    private services_Service services_service;




    private List<services_NetXResource> services_netxresources;


    public services_ServiceDistribution(
    ) {
        this.services_expressions = new ArrayList<>();
        this.services_netxresources = new ArrayList<>();
    }

    public services_ServiceDistribution(
        ArrayList<services_Expression> services_expressions,        ArrayList<services_NetXResource> services_netxresources    ) {
        this.services_expressions = services_expressions;
        this.services_netxresources = services_netxresources;
    }


    public List<services_Expression> getServices_expressions() {
        return services_expressions;
    }

    public void addServices_expression(Services_expression services_expression) {
        this.services_expressions.add(services_expression);
    }
    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }
    public List<services_NetXResource> getServices_netxresources() {
        return services_netxresources;
    }

    public void addServices_netxresource(Services_netxresource services_netxresource) {
        this.services_netxresources.add(services_netxresource);
    }

}