





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedBehavioredClassifier extends TracedClassifier {






    private List<uml_TracedInterfaceRealization> uml_tracedinterfacerealizations;


    public umlTrace_uml_TracedBehavioredClassifier(
    ) {
        super(
        );
        this.uml_tracedinterfacerealizations = new ArrayList<>();
    }

    public umlTrace_uml_TracedBehavioredClassifier(
        ArrayList<uml_TracedInterfaceRealization> uml_tracedinterfacerealizations    ) {
        this.uml_tracedinterfacerealizations = uml_tracedinterfacerealizations;
    }


    public List<uml_TracedInterfaceRealization> getUml_tracedinterfacerealizations() {
        return uml_tracedinterfacerealizations;
    }

    public void addUml_tracedinterfacerealization(Uml_tracedinterfacerealization uml_tracedinterfacerealization) {
        this.uml_tracedinterfacerealizations.add(uml_tracedinterfacerealization);
    }

}