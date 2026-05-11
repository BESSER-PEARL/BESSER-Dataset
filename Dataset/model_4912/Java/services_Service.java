





import java.util.List;
import java.util.ArrayList;

public class services_Service extends Base {

    private String serviceCategory;
    private String serviceName;
    private String serviceClass;
    private String serviceDescription;





    private List<services_ServiceForecast> services_serviceforecasts;




    private List<services_ServiceMonitor> services_servicemonitors;




    private List<services_ServiceUser> services_serviceusers;




    private services_ServiceDistribution services_servicedistribution;




    private List<services_Service> services_services;




    private List<services_CIID> services_ciids;


    public services_Service(
        String serviceCategory,        String serviceName,        String serviceClass,        String serviceDescription    ) {
        super(
        );
        this.serviceCategory = serviceCategory;
        this.serviceName = serviceName;
        this.serviceClass = serviceClass;
        this.serviceDescription = serviceDescription;
        this.services_serviceforecasts = new ArrayList<>();
        this.services_servicemonitors = new ArrayList<>();
        this.services_serviceusers = new ArrayList<>();
        this.services_services = new ArrayList<>();
        this.services_ciids = new ArrayList<>();
    }

    public services_Service(
        String serviceCategory,        String serviceName,        String serviceClass,        String serviceDescription        ArrayList<services_ServiceForecast> services_serviceforecasts,        ArrayList<services_ServiceMonitor> services_servicemonitors,        ArrayList<services_ServiceUser> services_serviceusers,        ArrayList<services_Service> services_services,        ArrayList<services_CIID> services_ciids    ) {
        this.serviceCategory = serviceCategory;
        this.serviceName = serviceName;
        this.serviceClass = serviceClass;
        this.serviceDescription = serviceDescription;
        this.services_serviceforecasts = services_serviceforecasts;
        this.services_servicemonitors = services_servicemonitors;
        this.services_serviceusers = services_serviceusers;
        this.services_services = services_services;
        this.services_ciids = services_ciids;
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
    public String getServiceclass() {
        return serviceClass;
    }

    public void setServiceclass(String serviceClass) {
        this.serviceClass = serviceClass;
    }
    public String getServicedescription() {
        return serviceDescription;
    }

    public void setServicedescription(String serviceDescription) {
        this.serviceDescription = serviceDescription;
    }

    public List<services_ServiceForecast> getServices_serviceforecasts() {
        return services_serviceforecasts;
    }

    public void addServices_serviceforecast(Services_serviceforecast services_serviceforecast) {
        this.services_serviceforecasts.add(services_serviceforecast);
    }
    public List<services_ServiceMonitor> getServices_servicemonitors() {
        return services_servicemonitors;
    }

    public void addServices_servicemonitor(Services_servicemonitor services_servicemonitor) {
        this.services_servicemonitors.add(services_servicemonitor);
    }
    public List<services_ServiceUser> getServices_serviceusers() {
        return services_serviceusers;
    }

    public void addServices_serviceuser(Services_serviceuser services_serviceuser) {
        this.services_serviceusers.add(services_serviceuser);
    }
    public services_ServiceDistribution getServices_servicedistribution() {
        return services_servicedistribution;
    }

    public void setServices_servicedistribution(services_ServiceDistribution services_servicedistribution) {
        this.services_servicedistribution = services_servicedistribution;
    }
    public List<services_Service> getServices_services() {
        return services_services;
    }

    public void addServices_service(Services_service services_service) {
        this.services_services.add(services_service);
    }
    public List<services_CIID> getServices_ciids() {
        return services_ciids;
    }

    public void addServices_ciid(Services_ciid services_ciid) {
        this.services_ciids.add(services_ciid);
    }

}