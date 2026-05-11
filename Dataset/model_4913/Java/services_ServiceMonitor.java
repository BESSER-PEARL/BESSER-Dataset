





import java.util.List;
import java.util.ArrayList;

public class services_ServiceMonitor extends Base {

    private String revision;
    private String name;





    private List<services_ResourceMonitor> services_resourcemonitors;




    private services_DateTimeRange services_datetimerange;


    public services_ServiceMonitor(
        String revision,        String name    ) {
        super(
        );
        this.revision = revision;
        this.name = name;
        this.services_resourcemonitors = new ArrayList<>();
    }

    public services_ServiceMonitor(
        String revision,        String name        ArrayList<services_ResourceMonitor> services_resourcemonitors    ) {
        this.revision = revision;
        this.name = name;
        this.services_resourcemonitors = services_resourcemonitors;
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

    public List<services_ResourceMonitor> getServices_resourcemonitors() {
        return services_resourcemonitors;
    }

    public void addServices_resourcemonitor(Services_resourcemonitor services_resourcemonitor) {
        this.services_resourcemonitors.add(services_resourcemonitor);
    }
    public services_DateTimeRange getServices_datetimerange() {
        return services_datetimerange;
    }

    public void setServices_datetimerange(services_DateTimeRange services_datetimerange) {
        this.services_datetimerange = services_datetimerange;
    }

}