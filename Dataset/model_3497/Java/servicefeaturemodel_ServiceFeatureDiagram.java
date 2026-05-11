





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_ServiceFeatureDiagram  {

    private String description;
    private String id;
    private String name;





    private servicefeaturemodel_Service servicefeaturemodel_service;


    public servicefeaturemodel_ServiceFeatureDiagram(
        String description,        String id,        String name    ) {
        this.description = description;
        this.id = id;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public servicefeaturemodel_Service getServicefeaturemodel_service() {
        return servicefeaturemodel_service;
    }

    public void setServicefeaturemodel_service(servicefeaturemodel_Service servicefeaturemodel_service) {
        this.servicefeaturemodel_service = servicefeaturemodel_service;
    }

}