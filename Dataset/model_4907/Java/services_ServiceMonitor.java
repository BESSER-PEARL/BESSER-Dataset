





import java.util.List;
import java.util.ArrayList;

public class services_ServiceMonitor  {

    private String name;
    private String revision;





    private services_Service services_service;


    public services_ServiceMonitor(
        String name,        String revision    ) {
        this.name = name;
        this.revision = revision;
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

}