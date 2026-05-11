





import java.util.List;
import java.util.ArrayList;

public class services_ServiceProfile  {

    private String name;





    private List<services_NetXResource> services_netxresources;




    private services_ServiceUser services_serviceuser;


    public services_ServiceProfile(
        String name    ) {
        this.name = name;
        this.services_netxresources = new ArrayList<>();
    }

    public services_ServiceProfile(
        String name        ArrayList<services_NetXResource> services_netxresources    ) {
        this.name = name;
        this.services_netxresources = services_netxresources;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<services_NetXResource> getServices_netxresources() {
        return services_netxresources;
    }

    public void addServices_netxresource(Services_netxresource services_netxresource) {
        this.services_netxresources.add(services_netxresource);
    }
    public services_ServiceUser getServices_serviceuser() {
        return services_serviceuser;
    }

    public void setServices_serviceuser(services_ServiceUser services_serviceuser) {
        this.services_serviceuser = services_serviceuser;
    }

}