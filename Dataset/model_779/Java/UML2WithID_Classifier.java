





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Classifier extends Element {






    private UML2WithID_Generalization uml2withid_generalization;




    private List<UML2WithID_Generalization> uml2withid_generalizations;


    public UML2WithID_Classifier(
    ) {
        super(
        );
        this.uml2withid_generalizations = new ArrayList<>();
    }

    public UML2WithID_Classifier(
        ArrayList<UML2WithID_Generalization> uml2withid_generalizations    ) {
        this.uml2withid_generalizations = uml2withid_generalizations;
    }


    public UML2WithID_Generalization getUml2withid_generalization() {
        return uml2withid_generalization;
    }

    public void setUml2withid_generalization(UML2WithID_Generalization uml2withid_generalization) {
        this.uml2withid_generalization = uml2withid_generalization;
    }
    public List<UML2WithID_Generalization> getUml2withid_generalizations() {
        return uml2withid_generalizations;
    }

    public void addUml2withid_generalization(Uml2withid_generalization uml2withid_generalization) {
        this.uml2withid_generalizations.add(uml2withid_generalization);
    }

}