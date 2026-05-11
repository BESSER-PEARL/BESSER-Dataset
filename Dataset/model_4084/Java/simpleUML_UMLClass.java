





import java.util.List;
import java.util.ArrayList;

public class simpleUML_UMLClass  {

    private String umlName;





    private simpleUML_Model simpleuml_model;




    private simpleUML_UMLClass simpleuml_umlclass;




    private simpleUML_Generalization simpleuml_generalization;




    private List<simpleUML_Generalization> simpleuml_generalizations;




    private List<simpleUML_UMLAttribute> simpleuml_umlattributes;


    public simpleUML_UMLClass(
        String umlName    ) {
        this.umlName = umlName;
        this.simpleuml_generalizations = new ArrayList<>();
        this.simpleuml_umlattributes = new ArrayList<>();
    }

    public simpleUML_UMLClass(
        String umlName        ArrayList<simpleUML_Generalization> simpleuml_generalizations,        ArrayList<simpleUML_UMLAttribute> simpleuml_umlattributes    ) {
        this.umlName = umlName;
        this.simpleuml_generalizations = simpleuml_generalizations;
        this.simpleuml_umlattributes = simpleuml_umlattributes;
    }

    public String getUmlname() {
        return umlName;
    }

    public void setUmlname(String umlName) {
        this.umlName = umlName;
    }

    public simpleUML_Model getSimpleuml_model() {
        return simpleuml_model;
    }

    public void setSimpleuml_model(simpleUML_Model simpleuml_model) {
        this.simpleuml_model = simpleuml_model;
    }
    public simpleUML_UMLClass getSimpleuml_umlclass() {
        return simpleuml_umlclass;
    }

    public void setSimpleuml_umlclass(simpleUML_UMLClass simpleuml_umlclass) {
        this.simpleuml_umlclass = simpleuml_umlclass;
    }
    public simpleUML_Generalization getSimpleuml_generalization() {
        return simpleuml_generalization;
    }

    public void setSimpleuml_generalization(simpleUML_Generalization simpleuml_generalization) {
        this.simpleuml_generalization = simpleuml_generalization;
    }
    public List<simpleUML_Generalization> getSimpleuml_generalizations() {
        return simpleuml_generalizations;
    }

    public void addSimpleuml_generalization(Simpleuml_generalization simpleuml_generalization) {
        this.simpleuml_generalizations.add(simpleuml_generalization);
    }
    public List<simpleUML_UMLAttribute> getSimpleuml_umlattributes() {
        return simpleuml_umlattributes;
    }

    public void addSimpleuml_umlattribute(Simpleuml_umlattribute simpleuml_umlattribute) {
        this.simpleuml_umlattributes.add(simpleuml_umlattribute);
    }

}