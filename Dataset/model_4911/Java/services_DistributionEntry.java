





import java.util.List;
import java.util.ArrayList;

public class services_DistributionEntry extends Base {

    private String resourceOrigin;





    private services_DerivedResource services_derivedresource;


    public services_DistributionEntry(
        String resourceOrigin    ) {
        super(
        );
        this.resourceOrigin = resourceOrigin;
    }


    public String getResourceorigin() {
        return resourceOrigin;
    }

    public void setResourceorigin(String resourceOrigin) {
        this.resourceOrigin = resourceOrigin;
    }

    public services_DerivedResource getServices_derivedresource() {
        return services_derivedresource;
    }

    public void setServices_derivedresource(services_DerivedResource services_derivedresource) {
        this.services_derivedresource = services_derivedresource;
    }

}