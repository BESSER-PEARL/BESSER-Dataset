





import java.util.List;
import java.util.ArrayList;

public class servicefeaturemodel_AttributeType  {

    private String scaleOrder;
    private boolean toBeEvaluated;
    private int customAttributeTypePriority;
    private String name;
    private String requirement;
    private String aggregationRule;
    private String domain;
    private String description;
    private String requirementWeight;





    private servicefeaturemodel_AttributeTypes servicefeaturemodel_attributetypes;




    private servicefeaturemodel_Attribute servicefeaturemodel_attribute;


    public servicefeaturemodel_AttributeType(
        String scaleOrder,        boolean toBeEvaluated,        int customAttributeTypePriority,        String name,        String requirement,        String aggregationRule,        String domain,        String description,        String requirementWeight    ) {
        this.scaleOrder = scaleOrder;
        this.toBeEvaluated = toBeEvaluated;
        this.customAttributeTypePriority = customAttributeTypePriority;
        this.name = name;
        this.requirement = requirement;
        this.aggregationRule = aggregationRule;
        this.domain = domain;
        this.description = description;
        this.requirementWeight = requirementWeight;
    }


    public String getScaleorder() {
        return scaleOrder;
    }

    public void setScaleorder(String scaleOrder) {
        this.scaleOrder = scaleOrder;
    }
    public boolean getTobeevaluated() {
        return toBeEvaluated;
    }

    public void setTobeevaluated(boolean toBeEvaluated) {
        this.toBeEvaluated = toBeEvaluated;
    }
    public int getCustomattributetypepriority() {
        return customAttributeTypePriority;
    }

    public void setCustomattributetypepriority(int customAttributeTypePriority) {
        this.customAttributeTypePriority = customAttributeTypePriority;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRequirement() {
        return requirement;
    }

    public void setRequirement(String requirement) {
        this.requirement = requirement;
    }
    public String getAggregationrule() {
        return aggregationRule;
    }

    public void setAggregationrule(String aggregationRule) {
        this.aggregationRule = aggregationRule;
    }
    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRequirementweight() {
        return requirementWeight;
    }

    public void setRequirementweight(String requirementWeight) {
        this.requirementWeight = requirementWeight;
    }

    public servicefeaturemodel_AttributeTypes getServicefeaturemodel_attributetypes() {
        return servicefeaturemodel_attributetypes;
    }

    public void setServicefeaturemodel_attributetypes(servicefeaturemodel_AttributeTypes servicefeaturemodel_attributetypes) {
        this.servicefeaturemodel_attributetypes = servicefeaturemodel_attributetypes;
    }
    public servicefeaturemodel_Attribute getServicefeaturemodel_attribute() {
        return servicefeaturemodel_attribute;
    }

    public void setServicefeaturemodel_attribute(servicefeaturemodel_Attribute servicefeaturemodel_attribute) {
        this.servicefeaturemodel_attribute = servicefeaturemodel_attribute;
    }

}