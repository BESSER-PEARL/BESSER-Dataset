





import java.util.List;
import java.util.ArrayList;

public class service_SL  {






    private List<service_ServiceConsumer> service_serviceconsumers;




    private List<service_Service> service_services;


    public service_SL(
    ) {
        this.service_serviceconsumers = new ArrayList<>();
        this.service_services = new ArrayList<>();
    }

    public service_SL(
        ArrayList<service_ServiceConsumer> service_serviceconsumers,        ArrayList<service_Service> service_services    ) {
        this.service_serviceconsumers = service_serviceconsumers;
        this.service_services = service_services;
    }


    public List<service_ServiceConsumer> getService_serviceconsumers() {
        return service_serviceconsumers;
    }

    public void addService_serviceconsumer(Service_serviceconsumer service_serviceconsumer) {
        this.service_serviceconsumers.add(service_serviceconsumer);
    }
    public List<service_Service> getService_services() {
        return service_services;
    }

    public void addService_service(Service_service service_service) {
        this.service_services.add(service_service);
    }

}