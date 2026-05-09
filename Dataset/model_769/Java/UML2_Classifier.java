





import java.util.List;
import java.util.ArrayList;

public class UML2_Classifier  {






    private List<UML2_Generalization> uml2_generalizations;




    private UML2_Generalization uml2_generalization;


    public UML2_Classifier(
    ) {
        this.uml2_generalizations = new ArrayList<>();
    }

    public UML2_Classifier(
        ArrayList<UML2_Generalization> uml2_generalizations    ) {
        this.uml2_generalizations = uml2_generalizations;
    }


    public List<UML2_Generalization> getUml2_generalizations() {
        return uml2_generalizations;
    }

    public void addUml2_generalization(Uml2_generalization uml2_generalization) {
        this.uml2_generalizations.add(uml2_generalization);
    }
    public UML2_Generalization getUml2_generalization() {
        return uml2_generalization;
    }

    public void setUml2_generalization(UML2_Generalization uml2_generalization) {
        this.uml2_generalization = uml2_generalization;
    }

}