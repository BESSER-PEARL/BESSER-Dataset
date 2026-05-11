





import java.util.List;
import java.util.ArrayList;

public class services_Service extends Base {

    private String serviceName;
    private String serviceCategory;
    private String serviceDescription;
    private String serviceClass;





    private List<services_ServiceMonitor> services_servicemonitors;




    private services_Service services_service;




    private List<services_CIID> services_ciids;


    public services_Service(
        String serviceName,        String serviceCategory,        String serviceDescription,        String serviceClass    ) {
        super(
        );
        this.serviceName = serviceName;
        this.serviceCategory = serviceCategory;
        this.serviceDescription = serviceDescription;
        this.serviceClass = serviceClass;
        this.services_servicemonitors = new ArrayList<>();
        this.services_ciids = new ArrayList<>();
    }

    public services_Service(
        String serviceName,        String serviceCategory,        String serviceDescription,        String serviceClass        ArrayList<services_ServiceMonitor> services_servicemonitors,        ArrayList<services_CIID> services_ciids    ) {
        this.serviceName = serviceName;
        this.serviceCategory = serviceCategory;
        this.serviceDescription = serviceDescription;
        this.serviceClass = serviceClass;
        this.services_servicemonitors = services_servicemonitors;
        this.services_ciids = services_ciids;
    }

    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }
    public String getServicecategory() {
        return serviceCategory;
    }

    public void setServicecategory(String serviceCategory) {
        this.serviceCategory = serviceCategory;
    }
    public String getServicedescription() {
        return serviceDescription;
    }

    public void setServicedescription(String serviceDescription) {
        this.serviceDescription = serviceDescription;
    }
    public String getServiceclass() {
        return serviceClass;
    }

    public void setServiceclass(String serviceClass) {
        this.serviceClass = serviceClass;
    }

    public List<services_ServiceMonitor> getServices_servicemonitors() {
        return services_servicemonitors;
    }

    public void addServices_servicemonitor(Services_servicemonitor services_servicemonitor) {
        this.services_servicemonitors.add(services_servicemonitor);
    }
    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }
    public List<services_CIID> getServices_ciids() {
        return services_ciids;
    }

    public void addServices_ciid(Services_ciid services_ciid) {
        this.services_ciids.add(services_ciid);
    }

}