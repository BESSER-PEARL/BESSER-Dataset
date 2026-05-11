





import java.util.List;
import java.util.ArrayList;

public class services_ServiceFlow extends Base {

    private String name;





    private List<services_ServiceFlowRelationship> services_serviceflowrelationships;




    private services_ServiceFlowRelationship services_serviceflowrelationship;


    public services_ServiceFlow(
        String name    ) {
        super(
        );
        this.name = name;
        this.services_serviceflowrelationships = new ArrayList<>();
    }

    public services_ServiceFlow(
        String name        ArrayList<services_ServiceFlowRelationship> services_serviceflowrelationships    ) {
        this.name = name;
        this.services_serviceflowrelationships = services_serviceflowrelationships;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<services_ServiceFlowRelationship> getServices_serviceflowrelationships() {
        return services_serviceflowrelationships;
    }

    public void addServices_serviceflowrelationship(Services_serviceflowrelationship services_serviceflowrelationship) {
        this.services_serviceflowrelationships.add(services_serviceflowrelationship);
    }
    public services_ServiceFlowRelationship getServices_serviceflowrelationship() {
        return services_serviceflowrelationship;
    }

    public void setServices_serviceflowrelationship(services_ServiceFlowRelationship services_serviceflowrelationship) {
        this.services_serviceflowrelationship = services_serviceflowrelationship;
    }

}