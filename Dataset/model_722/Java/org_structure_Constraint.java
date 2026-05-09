





import java.util.List;
import java.util.ArrayList;

public class org_structure_Constraint extends NamedElement {

    private String stereotype;
    private String language;





    private structure_ClassDefinition structure_classdefinition;




    private structure_Operation structure_operation;




    private structure_Operation structure_operation;


    public org_structure_Constraint(
        String stereotype,        String language    ) {
        super(
        );
        this.stereotype = stereotype;
        this.language = language;
    }


    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public structure_ClassDefinition getStructure_classdefinition() {
        return structure_classdefinition;
    }

    public void setStructure_classdefinition(structure_ClassDefinition structure_classdefinition) {
        this.structure_classdefinition = structure_classdefinition;
    }
    public structure_Operation getStructure_operation() {
        return structure_operation;
    }

    public void setStructure_operation(structure_Operation structure_operation) {
        this.structure_operation = structure_operation;
    }
    public structure_Operation getStructure_operation() {
        return structure_operation;
    }

    public void setStructure_operation(structure_Operation structure_operation) {
        this.structure_operation = structure_operation;
    }

}