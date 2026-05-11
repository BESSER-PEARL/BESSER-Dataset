





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedInteraction extends uml_TracedInteractionFragment, uml_TracedBehavior {






    private List<uml_TracedLifeline> uml_tracedlifelines;




    private List<uml_TracedMessage> uml_tracedmessages;




    private List<uml_TracedGate> uml_tracedgates;


    public umlTrace_uml_TracedInteraction(
    ) {
        super(
        );
        this.uml_tracedlifelines = new ArrayList<>();
        this.uml_tracedmessages = new ArrayList<>();
        this.uml_tracedgates = new ArrayList<>();
    }

    public umlTrace_uml_TracedInteraction(
        ArrayList<uml_TracedLifeline> uml_tracedlifelines,        ArrayList<uml_TracedMessage> uml_tracedmessages,        ArrayList<uml_TracedGate> uml_tracedgates    ) {
        this.uml_tracedlifelines = uml_tracedlifelines;
        this.uml_tracedmessages = uml_tracedmessages;
        this.uml_tracedgates = uml_tracedgates;
    }


    public List<uml_TracedLifeline> getUml_tracedlifelines() {
        return uml_tracedlifelines;
    }

    public void addUml_tracedlifeline(Uml_tracedlifeline uml_tracedlifeline) {
        this.uml_tracedlifelines.add(uml_tracedlifeline);
    }
    public List<uml_TracedMessage> getUml_tracedmessages() {
        return uml_tracedmessages;
    }

    public void addUml_tracedmessage(Uml_tracedmessage uml_tracedmessage) {
        this.uml_tracedmessages.add(uml_tracedmessage);
    }
    public List<uml_TracedGate> getUml_tracedgates() {
        return uml_tracedgates;
    }

    public void addUml_tracedgate(Uml_tracedgate uml_tracedgate) {
        this.uml_tracedgates.add(uml_tracedgate);
    }

}