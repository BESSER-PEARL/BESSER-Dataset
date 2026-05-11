





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_ResourceFilter  {

    private String resourcePattern;
    private String name;



    public camel_organisation_ResourceFilter(
        String resourcePattern,        String name    ) {
        this.resourcePattern = resourcePattern;
        this.name = name;
    }


    public String getResourcepattern() {
        return resourcePattern;
    }

    public void setResourcepattern(String resourcePattern) {
        this.resourcePattern = resourcePattern;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}