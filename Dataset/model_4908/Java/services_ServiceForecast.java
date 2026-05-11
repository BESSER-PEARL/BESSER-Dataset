





import java.util.List;
import java.util.ArrayList;

public class services_ServiceForecast extends Base {

    private String name;
    private String revision;





    private List<services_ResourceForecast> services_resourceforecasts;


    public services_ServiceForecast(
        String name,        String revision    ) {
        super(
        );
        this.name = name;
        this.revision = revision;
        this.services_resourceforecasts = new ArrayList<>();
    }

    public services_ServiceForecast(
        String name,        String revision        ArrayList<services_ResourceForecast> services_resourceforecasts    ) {
        this.name = name;
        this.revision = revision;
        this.services_resourceforecasts = services_resourceforecasts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }

    public List<services_ResourceForecast> getServices_resourceforecasts() {
        return services_resourceforecasts;
    }

    public void addServices_resourceforecast(Services_resourceforecast services_resourceforecast) {
        this.services_resourceforecasts.add(services_resourceforecast);
    }

}