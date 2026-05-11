





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_ServiceFeature  {

    private String requirementWeight;
    private boolean required;
    private String id;
    private String description;
    private String name;





    private servicefeaturemodel_ServiceFeature servicefeaturemodel_servicefeature;




    private servicefeaturemodel_ServiceFeatureDiagram servicefeaturemodel_servicefeaturediagram;


    public servicefeaturemodel_ServiceFeature(
        String requirementWeight,        boolean required,        String id,        String description,        String name    ) {
        this.requirementWeight = requirementWeight;
        this.required = required;
        this.id = id;
        this.description = description;
        this.name = name;
    }


    public String getRequirementweight() {
        return requirementWeight;
    }

    public void setRequirementweight(String requirementWeight) {
        this.requirementWeight = requirementWeight;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public servicefeaturemodel_ServiceFeature getServicefeaturemodel_servicefeature() {
        return servicefeaturemodel_servicefeature;
    }

    public void setServicefeaturemodel_servicefeature(servicefeaturemodel_ServiceFeature servicefeaturemodel_servicefeature) {
        this.servicefeaturemodel_servicefeature = servicefeaturemodel_servicefeature;
    }
    public servicefeaturemodel_ServiceFeatureDiagram getServicefeaturemodel_servicefeaturediagram() {
        return servicefeaturemodel_servicefeaturediagram;
    }

    public void setServicefeaturemodel_servicefeaturediagram(servicefeaturemodel_ServiceFeatureDiagram servicefeaturemodel_servicefeaturediagram) {
        this.servicefeaturemodel_servicefeaturediagram = servicefeaturemodel_servicefeaturediagram;
    }

}