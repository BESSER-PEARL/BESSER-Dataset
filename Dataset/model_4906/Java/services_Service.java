





import java.util.List;
import java.util.ArrayList;

public class services_Service  {

    private String serviceClass;
    private String serviceCategory;
    private String serviceName;
    private String serviceDescription;





    private services_Service services_service;




    private List<services_CIID> services_ciids;


    public services_Service(
        String serviceClass,        String serviceCategory,        String serviceName,        String serviceDescription    ) {
        this.serviceClass = serviceClass;
        this.serviceCategory = serviceCategory;
        this.serviceName = serviceName;
        this.serviceDescription = serviceDescription;
        this.services_ciids = new ArrayList<>();
    }

    public services_Service(
        String serviceClass,        String serviceCategory,        String serviceName,        String serviceDescription        ArrayList<services_CIID> services_ciids    ) {
        this.serviceClass = serviceClass;
        this.serviceCategory = serviceCategory;
        this.serviceName = serviceName;
        this.serviceDescription = serviceDescription;
        this.services_ciids = services_ciids;
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
    public String getServicename() {
        return serviceName;
    }

    public void setServicename(String serviceName) {
        this.serviceName = serviceName;
    }
    public String getServicedescription() {
        return serviceDescription;
    }

    public void setServicedescription(String serviceDescription) {
        this.serviceDescription = serviceDescription;
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