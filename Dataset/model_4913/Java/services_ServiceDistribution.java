





import java.util.List;
import java.util.ArrayList;

public class services_ServiceDistribution extends Base {






    private List<services_Expression> services_expressions;




    private services_Service services_service;


    public services_ServiceDistribution(
    ) {
        super(
        );
        this.services_expressions = new ArrayList<>();
    }

    public services_ServiceDistribution(
        ArrayList<services_Expression> services_expressions    ) {
        this.services_expressions = services_expressions;
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

}