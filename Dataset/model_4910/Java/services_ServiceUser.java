





import java.util.List;
import java.util.ArrayList;

public class services_ServiceUser extends Base {

    private String description;
    private String name;





    private services_Service services_service;




    private services_ServiceProfile services_serviceprofile;




    private services_ServiceForecastUsers services_serviceforecastusers;


    public services_ServiceUser(
        String description,        String name    ) {
        super(
        );
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public services_ServiceProfile getServices_serviceprofile() {
        return services_serviceprofile;
    }

    public void setServices_serviceprofile(services_ServiceProfile services_serviceprofile) {
        this.services_serviceprofile = services_serviceprofile;
    }
    public services_ServiceForecastUsers getServices_serviceforecastusers() {
        return services_serviceforecastusers;
    }

    public void setServices_serviceforecastusers(services_ServiceForecastUsers services_serviceforecastusers) {
        this.services_serviceforecastusers = services_serviceforecastusers;
    }

}