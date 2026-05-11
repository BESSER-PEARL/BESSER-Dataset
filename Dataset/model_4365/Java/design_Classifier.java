





import java.util.List;
import java.util.ArrayList;

public class design_Classifier  {

    private String name;
    private String accessModifier;





    private List<design_Attribute> design_attributes;




    private List<design_Operation> design_operations;




    private design_Design design_design;


    public design_Classifier(
        String name,        String accessModifier    ) {
        this.name = name;
        this.accessModifier = accessModifier;
        this.design_attributes = new ArrayList<>();
        this.design_operations = new ArrayList<>();
    }

    public design_Classifier(
        String name,        String accessModifier        ArrayList<design_Attribute> design_attributes,        ArrayList<design_Operation> design_operations    ) {
        this.name = name;
        this.accessModifier = accessModifier;
        this.design_attributes = design_attributes;
        this.design_operations = design_operations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccessmodifier() {
        return accessModifier;
    }

    public void setAccessmodifier(String accessModifier) {
        this.accessModifier = accessModifier;
    }

    public List<design_Attribute> getDesign_attributes() {
        return design_attributes;
    }

    public void addDesign_attribute(Design_attribute design_attribute) {
        this.design_attributes.add(design_attribute);
    }
    public List<design_Operation> getDesign_operations() {
        return design_operations;
    }

    public void addDesign_operation(Design_operation design_operation) {
        this.design_operations.add(design_operation);
    }
    public design_Design getDesign_design() {
        return design_design;
    }

    public void setDesign_design(design_Design design_design) {
        this.design_design = design_design;
    }

}