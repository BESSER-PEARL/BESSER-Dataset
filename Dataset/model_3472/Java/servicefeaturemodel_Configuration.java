





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_Configuration  {

    private String name;
    private String id;
    private boolean selected;
    private String description;





    private List<servicefeaturemodel_Attribute> servicefeaturemodel_attributes;




    private List<servicefeaturemodel_ServiceFeature> servicefeaturemodel_servicefeatures;




    private servicefeaturemodel_Configurations servicefeaturemodel_configurations;


    public servicefeaturemodel_Configuration(
        String name,        String id,        boolean selected,        String description    ) {
        this.name = name;
        this.id = id;
        this.selected = selected;
        this.description = description;
        this.servicefeaturemodel_attributes = new ArrayList<>();
        this.servicefeaturemodel_servicefeatures = new ArrayList<>();
    }

    public servicefeaturemodel_Configuration(
        String name,        String id,        boolean selected,        String description        ArrayList<servicefeaturemodel_Attribute> servicefeaturemodel_attributes,        ArrayList<servicefeaturemodel_ServiceFeature> servicefeaturemodel_servicefeatures    ) {
        this.name = name;
        this.id = id;
        this.selected = selected;
        this.description = description;
        this.servicefeaturemodel_attributes = servicefeaturemodel_attributes;
        this.servicefeaturemodel_servicefeatures = servicefeaturemodel_servicefeatures;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public servicefeaturemodel_Configurations getServicefeaturemodel_configurations() {
        return servicefeaturemodel_configurations;
    }

    public void setServicefeaturemodel_configurations(servicefeaturemodel_Configurations servicefeaturemodel_configurations) {
        this.servicefeaturemodel_configurations = servicefeaturemodel_configurations;
    }

}