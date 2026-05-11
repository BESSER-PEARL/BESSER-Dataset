





import java.util.List;
import java.util.ArrayList;

public class services_Service extends Base {

    private String serviceDescription;
    private String serviceName;
    private String serviceClass;
    private String serviceCategory;





    private List<services_CIID> services_ciids;




    private List<services_Service> services_services;




    private List<services_ServiceMonitor> services_servicemonitors;


    public services_Service(
        String serviceDescription,        String serviceName,        String serviceClass,        String serviceCategory    ) {
        super(
        );
        this.serviceDescription = serviceDescription;
        this.serviceName = serviceName;
        this.serviceClass = serviceClass;
        this.serviceCategory = serviceCategory;
        this.services_ciids = new ArrayList<>();
        this.services_services = new ArrayList<>();
        this.services_servicemonitors = new ArrayList<>();
    }

    public services_Service(
        String serviceDescription,        String serviceName,        String serviceClass,        String serviceCategory        ArrayList<services_CIID> services_ciids,        ArrayList<services_Service> services_services,        ArrayList<services_ServiceMonitor> services_servicemonitors    ) {
        this.serviceDescription = serviceDescription;
        this.serviceName = serviceName;
        this.serviceClass = serviceClass;
        this.serviceCategory = serviceCategory;
        this.services_ciids = services_ciids;
        this.services_services = services_services;
        this.services_servicemonitors = services_servicemonitors;
    }

    public String getServicedescription() {
        return serviceDescription;
    }

    public void setServicedescription(String serviceDescription) {
        this.serviceDescription = serviceDescription;
    }
    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }
    public String getServiceclass() {
        return serviceClass;
    }

    public void setServiceclass(String serviceClass) {
        this.serviceClass = serviceClass;
    }
    public String getServicecategory() {
        return serviceCategory;
    }

    public void setServicecategory(String serviceCategory) {
        this.serviceCategory = serviceCategory;
    }

    public List<services_CIID> getServices_ciids() {
        return services_ciids;
    }

    public void addServices_ciid(Services_ciid services_ciid) {
        this.services_ciids.add(services_ciid);
    }
    public List<services_Service> getServices_services() {
        return services_services;
    }

    public void addServices_service(Services_service services_service) {
        this.services_services.add(services_service);
    }
    public List<services_ServiceMonitor> getServices_servicemonitors() {
        return services_servicemonitors;
    }

    public void addServices_servicemonitor(Services_servicemonitor services_servicemonitor) {
        this.services_servicemonitors.add(services_servicemonitor);
    }

}