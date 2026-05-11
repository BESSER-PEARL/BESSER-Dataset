





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_Configuration  {

    private String name;
    private String description;
    private String id;





    private servicefeaturemodel_PossibleConfigurations servicefeaturemodel_possibleconfigurations;




    private List<servicefeaturemodel_Attribute> servicefeaturemodel_attributes;




    private List<servicefeaturemodel_ServiceFeature> servicefeaturemodel_servicefeatures;


    public servicefeaturemodel_Configuration(
        String name,        String description,        String id    ) {
        this.name = name;
        this.description = description;
        this.id = id;
        this.servicefeaturemodel_attributes = new ArrayList<>();
        this.servicefeaturemodel_servicefeatures = new ArrayList<>();
    }

    public servicefeaturemodel_Configuration(
        String name,        String description,        String id        ArrayList<servicefeaturemodel_Attribute> servicefeaturemodel_attributes,        ArrayList<servicefeaturemodel_ServiceFeature> servicefeaturemodel_servicefeatures    ) {
        this.name = name;
        this.description = description;
        this.id = id;
        this.servicefeaturemodel_attributes = servicefeaturemodel_attributes;
        this.servicefeaturemodel_servicefeatures = servicefeaturemodel_servicefeatures;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public servicefeaturemodel_PossibleConfigurations getServicefeaturemodel_possibleconfigurations() {
        return servicefeaturemodel_possibleconfigurations;
    }

    public void setServicefeaturemodel_possibleconfigurations(servicefeaturemodel_PossibleConfigurations servicefeaturemodel_possibleconfigurations) {
        this.servicefeaturemodel_possibleconfigurations = servicefeaturemodel_possibleconfigurations;
    }
    public List<servicefeaturemodel_Attribute> getServicefeaturemodel_attributes() {
        return servicefeaturemodel_attributes;
    }

    public void addServicefeaturemodel_attribute(Servicefeaturemodel_attribute servicefeaturemodel_attribute) {
        this.servicefeaturemodel_attributes.add(servicefeaturemodel_attribute);
    }
    public List<servicefeaturemodel_ServiceFeature> getServicefeaturemodel_servicefeatures() {
        return servicefeaturemodel_servicefeatures;
    }

    public void addServicefeaturemodel_servicefeature(Servicefeaturemodel_servicefeature servicefeaturemodel_servicefeature) {
        this.servicefeaturemodel_servicefeatures.add(servicefeaturemodel_servicefeature);
    }

}