





import java.util.List;
import java.util.ArrayList;

public class services_ServiceFlowRelationship extends Base {

    private String direction;





    private services_ServiceFlow services_serviceflow;




    private services_ServiceFlow services_serviceflow;




    private services_ReferenceRelationship services_referencerelationship;


    public services_ServiceFlowRelationship(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public services_ServiceFlow getServices_serviceflow() {
        return services_serviceflow;
    }

    public void setServices_serviceflow(services_ServiceFlow services_serviceflow) {
        this.services_serviceflow = services_serviceflow;
    }
    public services_ServiceFlow getServices_serviceflow() {
        return services_serviceflow;
    }

    public void setServices_serviceflow(services_ServiceFlow services_serviceflow) {
        this.services_serviceflow = services_serviceflow;
    }
    public services_ReferenceRelationship getServices_referencerelationship() {
        return services_referencerelationship;
    }

    public void setServices_referencerelationship(services_ReferenceRelationship services_referencerelationship) {
        this.services_referencerelationship = services_referencerelationship;
    }

}