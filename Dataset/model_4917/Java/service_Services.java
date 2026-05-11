





import java.util.List;
import java.util.ArrayList;

public class service_Services  {






    private List<service_Service> service_services;


    public service_Services(
    ) {
        this.service_services = new ArrayList<>();
    }

    public service_Services(
        ArrayList<service_Service> service_services    ) {
        this.service_services = service_services;
    }


    public List<service_Service> getService_services() {
        return service_services;
    }

    public void addService_service(Service_service service_service) {
        this.service_services.add(service_service);
    }

}