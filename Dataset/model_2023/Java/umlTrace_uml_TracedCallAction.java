





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedCallAction extends TracedInvocationAction {






    private List<uml_TracedOutputPin> uml_tracedoutputpins;


    public umlTrace_uml_TracedCallAction(
    ) {
        super(
        );
        this.uml_tracedoutputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedCallAction(
        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins    ) {
        this.uml_tracedoutputpins = uml_tracedoutputpins;
    }


    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }

}