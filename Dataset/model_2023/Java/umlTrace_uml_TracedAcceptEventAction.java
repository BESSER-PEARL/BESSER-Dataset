





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedAcceptEventAction extends TracedAction {






    private uml_umlTrace_AcceptEventAction uml_umltrace_accepteventaction;




    private List<uml_TracedOutputPin> uml_tracedoutputpins;




    private List<uml_TracedTrigger> uml_tracedtriggers;


    public umlTrace_uml_TracedAcceptEventAction(
    ) {
        super(
        );
        this.uml_tracedoutputpins = new ArrayList<>();
        this.uml_tracedtriggers = new ArrayList<>();
    }

    public umlTrace_uml_TracedAcceptEventAction(
        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins,        ArrayList<uml_TracedTrigger> uml_tracedtriggers    ) {
        this.uml_tracedoutputpins = uml_tracedoutputpins;
        this.uml_tracedtriggers = uml_tracedtriggers;
    }


    public uml_umlTrace_AcceptEventAction getUml_umltrace_accepteventaction() {
        return uml_umltrace_accepteventaction;
    }

    public void setUml_umltrace_accepteventaction(uml_umlTrace_AcceptEventAction uml_umltrace_accepteventaction) {
        this.uml_umltrace_accepteventaction = uml_umltrace_accepteventaction;
    }
    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }
    public List<uml_TracedTrigger> getUml_tracedtriggers() {
        return uml_tracedtriggers;
    }

    public void addUml_tracedtrigger(Uml_tracedtrigger uml_tracedtrigger) {
        this.uml_tracedtriggers.add(uml_tracedtrigger);
    }

}