





import java.util.List;
import java.util.ArrayList;

public class services_ServiceMonitor  {

    private String name;
    private String revision;





    private services_Service services_service;




    private List<services_ResourceMonitor> services_resourcemonitors;




    private services_DateTimeRange services_datetimerange;


    public services_ServiceMonitor(
        String name,        String revision    ) {
        this.name = name;
        this.revision = revision;
        this.services_resourcemonitors = new ArrayList<>();
    }

    public services_ServiceMonitor(
        String name,        String revision        ArrayList<services_ResourceMonitor> services_resourcemonitors    ) {
        this.name = name;
        this.revision = revision;
        this.services_resourcemonitors = services_resourcemonitors;
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

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
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