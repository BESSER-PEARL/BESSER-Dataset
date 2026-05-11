





import java.util.List;
import java.util.ArrayList;

public class uml_UML_BehavioredClassifier extends UML_Classifier {






    private List<uml_UML_InterfaceRealization> uml_uml_interfacerealizations;


    public uml_UML_BehavioredClassifier(
    ) {
        super(
        );
        this.uml_uml_interfacerealizations = new ArrayList<>();
    }

    public uml_UML_BehavioredClassifier(
        ArrayList<uml_UML_InterfaceRealization> uml_uml_interfacerealizations    ) {
        this.uml_uml_interfacerealizations = uml_uml_interfacerealizations;
    }


    public List<uml_UML_InterfaceRealization> getUml_uml_interfacerealizations() {
        return uml_uml_interfacerealizations;
    }

    public void addUml_uml_interfacerealization(Uml_uml_interfacerealization uml_uml_interfacerealization) {
        this.uml_uml_interfacerealizations.add(uml_uml_interfacerealization);
    }

}