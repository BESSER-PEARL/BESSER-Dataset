





import java.util.List;
import java.util.ArrayList;

public class services_ServiceUser extends Base {

    private String description;
    private String name;





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

    public services_ServiceForecastUsers getServices_serviceforecastusers() {
        return services_serviceforecastusers;
    }

    public void setServices_serviceforecastusers(services_ServiceForecastUsers services_serviceforecastusers) {
        this.services_serviceforecastusers = services_serviceforecastusers;
    }

}