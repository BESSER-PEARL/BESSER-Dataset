





import java.util.List;
import java.util.ArrayList;

public class ccore_UIValidator  {






    private ccore_TypeDefinition ccore_typedefinition;




    private List<ccore_Attribute> ccore_attributes;




    private List<ccore_UIValidator> ccore_uivalidators;


    public ccore_UIValidator(
    ) {
        this.ccore_attributes = new ArrayList<>();
        this.ccore_uivalidators = new ArrayList<>();
    }

    public ccore_UIValidator(
        ArrayList<ccore_Attribute> ccore_attributes,        ArrayList<ccore_UIValidator> ccore_uivalidators    ) {
        this.ccore_attributes = ccore_attributes;
        this.ccore_uivalidators = ccore_uivalidators;
    }


    public ccore_TypeDefinition getCcore_typedefinition() {
        return ccore_typedefinition;
    }

    public void setCcore_typedefinition(ccore_TypeDefinition ccore_typedefinition) {
        this.ccore_typedefinition = ccore_typedefinition;
    }
    public List<ccore_Attribute> getCcore_attributes() {
        return ccore_attributes;
    }

    public void addCcore_attribute(Ccore_attribute ccore_attribute) {
        this.ccore_attributes.add(ccore_attribute);
    }
    public List<ccore_UIValidator> getCcore_uivalidators() {
        return ccore_uivalidators;
    }

    public void addCcore_uivalidator(Ccore_uivalidator ccore_uivalidator) {
        this.ccore_uivalidators.add(ccore_uivalidator);
    }

}