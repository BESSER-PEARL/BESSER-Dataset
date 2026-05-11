





import java.util.List;
import java.util.ArrayList;

public class services_ServiceSupport  {

    private String supportDays;
    private String supportHours;





    private services_Service services_service;


    public services_ServiceSupport(
        String supportDays,        String supportHours    ) {
        this.supportDays = supportDays;
        this.supportHours = supportHours;
    }


    public String getSupportdays() {
        return supportDays;
    }

    public void setSupportdays(String supportDays) {
        this.supportDays = supportDays;
    }
    public String getSupporthours() {
        return supportHours;
    }

    public void setSupporthours(String supportHours) {
        this.supportHours = supportHours;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}