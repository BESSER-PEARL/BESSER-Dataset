





import java.util.List;
import java.util.ArrayList;

public class service_ServiceConsumer extends Agent {

    private String isType;





    private List<service_Service> service_services;


    public service_ServiceConsumer(
        String isType    ) {
        super(
        );
        this.isType = isType;
        this.service_services = new ArrayList<>();
    }

    public service_ServiceConsumer(
        String isType        ArrayList<service_Service> service_services    ) {
        this.isType = isType;
        this.service_services = service_services;
    }

    public String getIstype() {
        return isType;
    }

    public void setIstype(String isType) {
        this.isType = isType;
    }

    public List<service_Service> getService_services() {
        return service_services;
    }

    public void addService_service(Service_service service_service) {
        this.service_services.add(service_service);
    }

}