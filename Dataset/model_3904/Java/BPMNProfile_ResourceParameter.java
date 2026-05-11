





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ResourceParameter extends BaseElement {

    private String isRequired;





    private BPMNProfile_Resource bpmnprofile_resource;




    private BPMNProfile_ItemDefinition bpmnprofile_itemdefinition;




    private BPMNProfile_ResourceParameterBinding bpmnprofile_resourceparameterbinding;


    public BPMNProfile_ResourceParameter(
        String isRequired    ) {
        super(
        );
        this.isRequired = isRequired;
    }


    public String getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(String isRequired) {
        this.isRequired = isRequired;
    }

    public BPMNProfile_Resource getBpmnprofile_resource() {
        return bpmnprofile_resource;
    }

    public void setBpmnprofile_resource(BPMNProfile_Resource bpmnprofile_resource) {
        this.bpmnprofile_resource = bpmnprofile_resource;
    }
    public BPMNProfile_ItemDefinition getBpmnprofile_itemdefinition() {
        return bpmnprofile_itemdefinition;
    }

    public void setBpmnprofile_itemdefinition(BPMNProfile_ItemDefinition bpmnprofile_itemdefinition) {
        this.bpmnprofile_itemdefinition = bpmnprofile_itemdefinition;
    }
    public BPMNProfile_ResourceParameterBinding getBpmnprofile_resourceparameterbinding() {
        return bpmnprofile_resourceparameterbinding;
    }

    public void setBpmnprofile_resourceparameterbinding(BPMNProfile_ResourceParameterBinding bpmnprofile_resourceparameterbinding) {
        this.bpmnprofile_resourceparameterbinding = bpmnprofile_resourceparameterbinding;
    }

}