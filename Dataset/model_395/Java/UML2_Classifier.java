





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier extends Namespace, RedefinableElement, Type {






    private UML2_Generalization uml2_generalization;




    private List<UML2_Generalization> uml2_generalizations;




    private List<UML2_NamedElement> uml2_namedelements;


    public UML2_Classifier(
    ) {
        super(
        );
        this.uml2_generalizations = new ArrayList<>();
        this.uml2_namedelements = new ArrayList<>();
    }

    public UML2_Classifier(
        ArrayList<UML2_Generalization> uml2_generalizations,        ArrayList<UML2_NamedElement> uml2_namedelements    ) {
        this.uml2_generalizations = uml2_generalizations;
        this.uml2_namedelements = uml2_namedelements;
    }


    public UML2_Generalization getUml2_generalization() {
        return uml2_generalization;
    }

    public void setUml2_generalization(UML2_Generalization uml2_generalization) {
        this.uml2_generalization = uml2_generalization;
    }
    public List<UML2_Generalization> getUml2_generalizations() {
        return uml2_generalizations;
    }

    public void addUml2_generalization(Uml2_generalization uml2_generalization) {
        this.uml2_generalizations.add(uml2_generalization);
    }
    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }

}