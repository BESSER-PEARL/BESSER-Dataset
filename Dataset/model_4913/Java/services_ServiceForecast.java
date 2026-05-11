





import java.util.List;
import java.util.ArrayList;

public class services_ServiceForecast extends Base {

    private String revision;
    private String name;





    private services_Service services_service;




    private List<services_ResourceForecast> services_resourceforecasts;




    private List<services_ServiceForecastUsers> services_serviceforecastuserss;




    private services_DateTimeRange services_datetimerange;


    public services_ServiceForecast(
        String revision,        String name    ) {
        super(
        );
        this.revision = revision;
        this.name = name;
        this.services_resourceforecasts = new ArrayList<>();
        this.services_serviceforecastuserss = new ArrayList<>();
    }

    public services_ServiceForecast(
        String revision,        String name        ArrayList<services_ResourceForecast> services_resourceforecasts,        ArrayList<services_ServiceForecastUsers> services_serviceforecastuserss    ) {
        this.revision = revision;
        this.name = name;
        this.services_resourceforecasts = services_resourceforecasts;
        this.services_serviceforecastuserss = services_serviceforecastuserss;
    }

    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
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
    public List<services_ResourceForecast> getServices_resourceforecasts() {
        return services_resourceforecasts;
    }

    public void addServices_resourceforecast(Services_resourceforecast services_resourceforecast) {
        this.services_resourceforecasts.add(services_resourceforecast);
    }
    public List<services_ServiceForecastUsers> getServices_serviceforecastuserss() {
        return services_serviceforecastuserss;
    }

    public void addServices_serviceforecastusers(Services_serviceforecastusers services_serviceforecastusers) {
        this.services_serviceforecastuserss.add(services_serviceforecastusers);
    }
    public services_DateTimeRange getServices_datetimerange() {
        return services_datetimerange;
    }

    public void setServices_datetimerange(services_DateTimeRange services_datetimerange) {
        this.services_datetimerange = services_datetimerange;
    }

}