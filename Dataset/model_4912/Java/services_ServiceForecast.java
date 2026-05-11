





import java.util.List;
import java.util.ArrayList;

public class services_ServiceForecast extends Base {

    private String revision;
    private String name;





    private List<services_ServiceForecastUsers> services_serviceforecastuserss;


    public services_ServiceForecast(
        String revision,        String name    ) {
        super(
        );
        this.revision = revision;
        this.name = name;
        this.services_serviceforecastuserss = new ArrayList<>();
    }

    public services_ServiceForecast(
        String revision,        String name        ArrayList<services_ServiceForecastUsers> services_serviceforecastuserss    ) {
        this.revision = revision;
        this.name = name;
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

    public List<services_ServiceForecastUsers> getServices_serviceforecastuserss() {
        return services_serviceforecastuserss;
    }

    public void addServices_serviceforecastusers(Services_serviceforecastusers services_serviceforecastusers) {
        this.services_serviceforecastuserss.add(services_serviceforecastusers);
    }

}