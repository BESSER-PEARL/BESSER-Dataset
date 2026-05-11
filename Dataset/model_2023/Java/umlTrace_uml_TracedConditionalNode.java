





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedConditionalNode extends TracedStructuredActivityNode {






    private List<uml_TracedOutputPin> uml_tracedoutputpins;




    private List<uml_TracedClause> uml_tracedclauses;


    public umlTrace_uml_TracedConditionalNode(
    ) {
        super(
        );
        this.uml_tracedoutputpins = new ArrayList<>();
        this.uml_tracedclauses = new ArrayList<>();
    }

    public umlTrace_uml_TracedConditionalNode(
        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins,        ArrayList<uml_TracedClause> uml_tracedclauses    ) {
        this.uml_tracedoutputpins = uml_tracedoutputpins;
        this.uml_tracedclauses = uml_tracedclauses;
    }


    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }
    public List<uml_TracedClause> getUml_tracedclauses() {
        return uml_tracedclauses;
    }

    public void addUml_tracedclause(Uml_tracedclause uml_tracedclause) {
        this.uml_tracedclauses.add(uml_tracedclause);
    }

}