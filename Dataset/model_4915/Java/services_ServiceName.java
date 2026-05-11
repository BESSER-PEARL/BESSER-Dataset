





import java.util.List;
import java.util.ArrayList;

public class services_ServiceName  {

    private String alias;
    private String identifier;
    private String name;
    private String index;





    private services_Service services_service;


    public services_ServiceName(
        String alias,        String identifier,        String name,        String index    ) {
        this.alias = alias;
        this.identifier = identifier;
        this.name = name;
        this.index = index;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}