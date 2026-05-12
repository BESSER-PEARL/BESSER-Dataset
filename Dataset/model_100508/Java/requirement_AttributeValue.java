





import java.util.List;
import java.util.ArrayList;

public class requirement_AttributeValue  {

    private String value;





    private requirement_DefaultAttributeValue requirement_defaultattributevalue;




    private requirement_ConfiguratedAttribute requirement_configuratedattribute;


    public requirement_AttributeValue(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public requirement_DefaultAttributeValue getRequirement_defaultattributevalue() {
        return requirement_defaultattributevalue;
    }

    public void setRequirement_defaultattributevalue(requirement_DefaultAttributeValue requirement_defaultattributevalue) {
        this.requirement_defaultattributevalue = requirement_defaultattributevalue;
    }
    public requirement_ConfiguratedAttribute getRequirement_configuratedattribute() {
        return requirement_configuratedattribute;
    }

    public void setRequirement_configuratedattribute(requirement_ConfiguratedAttribute requirement_configuratedattribute) {
        this.requirement_configuratedattribute = requirement_configuratedattribute;
    }

}