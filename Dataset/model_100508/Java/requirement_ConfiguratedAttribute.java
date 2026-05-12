





import java.util.List;
import java.util.ArrayList;

public class requirement_ConfiguratedAttribute  {

    private String name;
    private String type;





    private requirement_AttributeConfiguration requirement_attributeconfiguration;


    public requirement_ConfiguratedAttribute(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public requirement_AttributeConfiguration getRequirement_attributeconfiguration() {
        return requirement_attributeconfiguration;
    }

    public void setRequirement_attributeconfiguration(requirement_AttributeConfiguration requirement_attributeconfiguration) {
        this.requirement_attributeconfiguration = requirement_attributeconfiguration;
    }

}