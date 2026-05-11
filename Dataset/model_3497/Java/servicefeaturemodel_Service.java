





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_Service  {

    private String name;
    private String description;
    private String id;





    private servicefeaturemodel_AttributeTypes servicefeaturemodel_attributetypes;




    private servicefeaturemodel_PossibleConfigurations servicefeaturemodel_possibleconfigurations;


    public servicefeaturemodel_Service(
        String name,        String description,        String id    ) {
        this.name = name;
        this.description = description;
        this.id = id;
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

    public servicefeaturemodel_AttributeTypes getServicefeaturemodel_attributetypes() {
        return servicefeaturemodel_attributetypes;
    }

    public void setServicefeaturemodel_attributetypes(servicefeaturemodel_AttributeTypes servicefeaturemodel_attributetypes) {
        this.servicefeaturemodel_attributetypes = servicefeaturemodel_attributetypes;
    }
    public servicefeaturemodel_PossibleConfigurations getServicefeaturemodel_possibleconfigurations() {
        return servicefeaturemodel_possibleconfigurations;
    }

    public void setServicefeaturemodel_possibleconfigurations(servicefeaturemodel_PossibleConfigurations servicefeaturemodel_possibleconfigurations) {
        this.servicefeaturemodel_possibleconfigurations = servicefeaturemodel_possibleconfigurations;
    }

}