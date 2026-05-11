





import java.util.List;
import java.util.ArrayList;

public class services_Service  {

    private String serviceCategory;
    private String serviceDescription;
    private String serviceClass;
    private String serviceName;





    private List<services_CIID> services_ciids;




    private services_Service services_service;


    public services_Service(
        String serviceCategory,        String serviceDescription,        String serviceClass,        String serviceName    ) {
        this.serviceCategory = serviceCategory;
        this.serviceDescription = serviceDescription;
        this.serviceClass = serviceClass;
        this.serviceName = serviceName;
        this.services_ciids = new ArrayList<>();
    }

    public services_Service(
        String serviceCategory,        String serviceDescription,        String serviceClass,        String serviceName        ArrayList<services_CIID> services_ciids    ) {
        this.serviceCategory = serviceCategory;
        this.serviceDescription = serviceDescription;
        this.serviceClass = serviceClass;
        this.serviceName = serviceName;
        this.services_ciids = services_ciids;
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
    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }

    public List<services_CIID> getServices_ciids() {
        return services_ciids;
    }

    public void addServices_ciid(Services_ciid services_ciid) {
        this.services_ciids.add(services_ciid);
    }
    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}