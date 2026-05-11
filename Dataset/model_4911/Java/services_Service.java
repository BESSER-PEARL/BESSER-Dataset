





import java.util.List;
import java.util.ArrayList;

public class services_Service extends Base {

    private String serviceDescription;
    private String serviceName;
    private String serviceClass;
    private String serviceCategory;





    private services_Lifecycle services_lifecycle;




    private List<services_ServiceForecast> services_serviceforecasts;




    private List<services_ServiceMonitor> services_servicemonitors;




    private List<services_Service> services_services;




    private List<services_ServiceUser> services_serviceusers;


    public services_Service(
        String serviceDescription,        String serviceName,        String serviceClass,        String serviceCategory    ) {
        super(
        );
        this.serviceDescription = serviceDescription;
        this.serviceName = serviceName;
        this.serviceClass = serviceClass;
        this.serviceCategory = serviceCategory;
        this.services_serviceforecasts = new ArrayList<>();
        this.services_servicemonitors = new ArrayList<>();
        this.services_services = new ArrayList<>();
        this.services_serviceusers = new ArrayList<>();
    }

    public services_Service(
        String serviceDescription,        String serviceName,        String serviceClass,        String serviceCategory        ArrayList<services_ServiceForecast> services_serviceforecasts,        ArrayList<services_ServiceMonitor> services_servicemonitors,        ArrayList<services_Service> services_services,        ArrayList<services_ServiceUser> services_serviceusers    ) {
        this.serviceDescription = serviceDescription;
        this.serviceName = serviceName;
        this.serviceClass = serviceClass;
        this.serviceCategory = serviceCategory;
        this.services_serviceforecasts = services_serviceforecasts;
        this.services_servicemonitors = services_servicemonitors;
        this.services_services = services_services;
        this.services_serviceusers = services_serviceusers;
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

    public services_Lifecycle getServices_lifecycle() {
        return services_lifecycle;
    }

    public void setServices_lifecycle(services_Lifecycle services_lifecycle) {
        this.services_lifecycle = services_lifecycle;
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
    public List<services_Service> getServices_services() {
        return services_services;
    }

    public void addServices_service(Services_service services_service) {
        this.services_services.add(services_service);
    }
    public List<services_ServiceUser> getServices_serviceusers() {
        return services_serviceusers;
    }

    public void addServices_serviceuser(Services_serviceuser services_serviceuser) {
        this.services_serviceusers.add(services_serviceuser);
    }

}