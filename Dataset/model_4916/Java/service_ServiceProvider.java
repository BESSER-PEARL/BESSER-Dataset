





import java.util.List;
import java.util.ArrayList;

public class service_ServiceProvider extends Agent {

    private String isType;





    private List<service_Service> service_services;




    private service_SL service_sl;




    private List<service_ServiceImplemetation> service_serviceimplemetations;


    public service_ServiceProvider(
        String isType    ) {
        super(
        );
        this.isType = isType;
        this.service_services = new ArrayList<>();
        this.service_serviceimplemetations = new ArrayList<>();
    }

    public service_ServiceProvider(
        String isType        ArrayList<service_Service> service_services,        ArrayList<service_ServiceImplemetation> service_serviceimplemetations    ) {
        this.isType = isType;
        this.service_services = service_services;
        this.service_serviceimplemetations = service_serviceimplemetations;
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
    public service_SL getService_sl() {
        return service_sl;
    }

    public void setService_sl(service_SL service_sl) {
        this.service_sl = service_sl;
    }
    public List<service_ServiceImplemetation> getService_serviceimplemetations() {
        return service_serviceimplemetations;
    }

    public void addService_serviceimplemetation(Service_serviceimplemetation service_serviceimplemetation) {
        this.service_serviceimplemetations.add(service_serviceimplemetation);
    }

}