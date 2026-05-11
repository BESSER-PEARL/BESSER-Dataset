





import java.util.List;
import java.util.ArrayList;

public class services_ServiceName  {

    private String identifier;
    private String alias;
    private String index;
    private String name;





    private services_Service services_service;


    public services_ServiceName(
        String identifier,        String alias,        String index,        String name    ) {
        this.identifier = identifier;
        this.alias = alias;
        this.index = index;
        this.name = name;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}