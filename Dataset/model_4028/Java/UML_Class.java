





import java.util.List;
import java.util.ArrayList;

public class UML_Class extends Package {






    private List<UML_Generalization> uml_generalizations;




    private UML_Generalization uml_generalization;




    private UML_Class uml_class;




    private UML_Generalization uml_generalization;




    private List<UML_TemplateBinding> uml_templatebindings;


    public UML_Class(
    ) {
        super(
        );
        this.uml_generalizations = new ArrayList<>();
        this.uml_templatebindings = new ArrayList<>();
    }

    public UML_Class(
        ArrayList<UML_Generalization> uml_generalizations,        ArrayList<UML_TemplateBinding> uml_templatebindings    ) {
        this.uml_generalizations = uml_generalizations;
        this.uml_templatebindings = uml_templatebindings;
    }


    public List<UML_Generalization> getUml_generalizations() {
        return uml_generalizations;
    }

    public void addUml_generalization(Uml_generalization uml_generalization) {
        this.uml_generalizations.add(uml_generalization);
    }
    public UML_Generalization getUml_generalization() {
        return uml_generalization;
    }

    public void setUml_generalization(UML_Generalization uml_generalization) {
        this.uml_generalization = uml_generalization;
    }
    public UML_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(UML_Class uml_class) {
        this.uml_class = uml_class;
    }
    public UML_Generalization getUml_generalization() {
        return uml_generalization;
    }

    public void setUml_generalization(UML_Generalization uml_generalization) {
        this.uml_generalization = uml_generalization;
    }
    public List<UML_TemplateBinding> getUml_templatebindings() {
        return uml_templatebindings;
    }

    public void addUml_templatebinding(Uml_templatebinding uml_templatebinding) {
        this.uml_templatebindings.add(uml_templatebinding);
    }

}