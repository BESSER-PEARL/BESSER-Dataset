





import java.util.List;
import java.util.ArrayList;

public class UMLMM_BehavioredClassifier extends Classifier {






    private List<UMLMM_InterfaceRealization> umlmm_interfacerealizations;


    public UMLMM_BehavioredClassifier(
    ) {
        super(
        );
        this.umlmm_interfacerealizations = new ArrayList<>();
    }

    public UMLMM_BehavioredClassifier(
        ArrayList<UMLMM_InterfaceRealization> umlmm_interfacerealizations    ) {
        this.umlmm_interfacerealizations = umlmm_interfacerealizations;
    }


    public List<UMLMM_InterfaceRealization> getUmlmm_interfacerealizations() {
        return umlmm_interfacerealizations;
    }

    public void addUmlmm_interfacerealization(Umlmm_interfacerealization umlmm_interfacerealization) {
        this.umlmm_interfacerealizations.add(umlmm_interfacerealization);
    }

}