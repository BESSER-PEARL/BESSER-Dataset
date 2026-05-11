





import java.util.List;
import java.util.ArrayList;

public class commons_ResourceAware  {

    private String resourceUri;
    private String resourceName;
    private String resourceType;



    public commons_ResourceAware(
        String resourceUri,        String resourceName,        String resourceType    ) {
        this.resourceUri = resourceUri;
        this.resourceName = resourceName;
        this.resourceType = resourceType;
    }


    public String getResourceuri() {
        return resourceUri;
    }

    public void setResourceuri(String resourceUri) {
        this.resourceUri = resourceUri;
    }
    public String getResourcename() {
        return resourceName;
    }

    public void setResourcename(String resourceName) {
        this.resourceName = resourceName;
    }
    public String getResourcetype() {
        return resourceType;
    }

    public void setResourcetype(String resourceType) {
        this.resourceType = resourceType;
    }


}