





import java.util.List;
import java.util.ArrayList;

public class services_ServiceUser  {

    private String name;





    private services_Service services_service;


    public services_ServiceUser(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}