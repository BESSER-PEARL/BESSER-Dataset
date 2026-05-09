





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Constraint extends NamedElement {

    private String language;
    private String stereotype;





    private structure_Operation structure_operation;




    private structure_Operation structure_operation;




    private behavior_Expression behavior_expression;




    private structure_ClassDefinition structure_classdefinition;


    public kermeta_structure_Constraint(
        String language,        String stereotype    ) {
        super(
        );
        this.language = language;
        this.stereotype = stereotype;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getStereotype() {
        return stereotype;
    }

    public void setStereotype(String stereotype) {
        this.stereotype = stereotype;
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
    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }
    public structure_ClassDefinition getStructure_classdefinition() {
        return structure_classdefinition;
    }

    public void setStructure_classdefinition(structure_ClassDefinition structure_classdefinition) {
        this.structure_classdefinition = structure_classdefinition;
    }

}