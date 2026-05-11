





import java.util.List;
import java.util.ArrayList;

public class services_ServiceProfile extends Base {

    private String name;





    private List<services_DerivedResource> services_derivedresources;




    private services_ServiceUser services_serviceuser;


    public services_ServiceProfile(
        String name    ) {
        super(
        );
        this.name = name;
        this.services_derivedresources = new ArrayList<>();
    }

    public services_ServiceProfile(
        String name        ArrayList<services_DerivedResource> services_derivedresources    ) {
        this.name = name;
        this.services_derivedresources = services_derivedresources;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<services_DerivedResource> getServices_derivedresources() {
        return services_derivedresources;
    }

    public void addServices_derivedresource(Services_derivedresource services_derivedresource) {
        this.services_derivedresources.add(services_derivedresource);
    }
    public services_ServiceUser getServices_serviceuser() {
        return services_serviceuser;
    }

    public void setServices_serviceuser(services_ServiceUser services_serviceuser) {
        this.services_serviceuser = services_serviceuser;
    }

}