





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedProtocolStateMachine extends TracedStateMachine {






    private List<uml_TracedProtocolConformance> uml_tracedprotocolconformances;


    public umlTrace_uml_TracedProtocolStateMachine(
    ) {
        super(
        );
        this.uml_tracedprotocolconformances = new ArrayList<>();
    }

    public umlTrace_uml_TracedProtocolStateMachine(
        ArrayList<uml_TracedProtocolConformance> uml_tracedprotocolconformances    ) {
        this.uml_tracedprotocolconformances = uml_tracedprotocolconformances;
    }


    public List<uml_TracedProtocolConformance> getUml_tracedprotocolconformances() {
        return uml_tracedprotocolconformances;
    }

    public void addUml_tracedprotocolconformance(Uml_tracedprotocolconformance uml_tracedprotocolconformance) {
        this.uml_tracedprotocolconformances.add(uml_tracedprotocolconformance);
    }

}