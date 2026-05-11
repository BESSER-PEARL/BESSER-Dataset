





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_AttributeToAttributeModifyRelationship extends ModifyRelationship {

    private String triggerParameterName;





    private servicefeaturemodel_Attribute servicefeaturemodel_attribute;


    public servicefeaturemodel_AttributeToAttributeModifyRelationship(
        String triggerParameterName    ) {
        super(
        );
        this.triggerParameterName = triggerParameterName;
    }


    public String getTriggerparametername() {
        return triggerParameterName;
    }

    public void setTriggerparametername(String triggerParameterName) {
        this.triggerParameterName = triggerParameterName;
    }

    public servicefeaturemodel_Attribute getServicefeaturemodel_attribute() {
        return servicefeaturemodel_attribute;
    }

    public void setServicefeaturemodel_attribute(servicefeaturemodel_Attribute servicefeaturemodel_attribute) {
        this.servicefeaturemodel_attribute = servicefeaturemodel_attribute;
    }

}