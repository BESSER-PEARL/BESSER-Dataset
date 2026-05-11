





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedEncapsulatedClassifier extends TracedStructuredClassifier {






    private List<uml_TracedPort> uml_tracedports;


    public umlTrace_uml_TracedEncapsulatedClassifier(
    ) {
        super(
        );
        this.uml_tracedports = new ArrayList<>();
    }

    public umlTrace_uml_TracedEncapsulatedClassifier(
        ArrayList<uml_TracedPort> uml_tracedports    ) {
        this.uml_tracedports = uml_tracedports;
    }


    public List<uml_TracedPort> getUml_tracedports() {
        return uml_tracedports;
    }

    public void addUml_tracedport(Uml_tracedport uml_tracedport) {
        this.uml_tracedports.add(uml_tracedport);
    }

}