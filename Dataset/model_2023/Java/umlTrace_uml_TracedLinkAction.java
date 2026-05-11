





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedLinkAction extends TracedAction {






    private List<uml_TracedLinkEndData> uml_tracedlinkenddatas;




    private List<uml_TracedInputPin> uml_tracedinputpins;


    public umlTrace_uml_TracedLinkAction(
    ) {
        super(
        );
        this.uml_tracedlinkenddatas = new ArrayList<>();
        this.uml_tracedinputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedLinkAction(
        ArrayList<uml_TracedLinkEndData> uml_tracedlinkenddatas,        ArrayList<uml_TracedInputPin> uml_tracedinputpins    ) {
        this.uml_tracedlinkenddatas = uml_tracedlinkenddatas;
        this.uml_tracedinputpins = uml_tracedinputpins;
    }


    public List<uml_TracedLinkEndData> getUml_tracedlinkenddatas() {
        return uml_tracedlinkenddatas;
    }

    public void addUml_tracedlinkenddata(Uml_tracedlinkenddata uml_tracedlinkenddata) {
        this.uml_tracedlinkenddatas.add(uml_tracedlinkenddata);
    }
    public List<uml_TracedInputPin> getUml_tracedinputpins() {
        return uml_tracedinputpins;
    }

    public void addUml_tracedinputpin(Uml_tracedinputpin uml_tracedinputpin) {
        this.uml_tracedinputpins.add(uml_tracedinputpin);
    }

}