





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedClause extends TracedElement {






    private List<uml_TracedClause> uml_tracedclauses;




    private List<uml_TracedClause> uml_tracedclauses;




    private uml_TracedOutputPin uml_tracedoutputpin;




    private List<uml_TracedOutputPin> uml_tracedoutputpins;


    public umlTrace_uml_TracedClause(
    ) {
        super(
        );
        this.uml_tracedclauses = new ArrayList<>();
        this.uml_tracedclauses = new ArrayList<>();
        this.uml_tracedoutputpins = new ArrayList<>();
    }

    public umlTrace_uml_TracedClause(
        ArrayList<uml_TracedClause> uml_tracedclauses,        ArrayList<uml_TracedClause> uml_tracedclauses,        ArrayList<uml_TracedOutputPin> uml_tracedoutputpins    ) {
        this.uml_tracedclauses = uml_tracedclauses;
        this.uml_tracedclauses = uml_tracedclauses;
        this.uml_tracedoutputpins = uml_tracedoutputpins;
    }


    public List<uml_TracedClause> getUml_tracedclauses() {
        return uml_tracedclauses;
    }

    public void addUml_tracedclause(Uml_tracedclause uml_tracedclause) {
        this.uml_tracedclauses.add(uml_tracedclause);
    }
    public List<uml_TracedClause> getUml_tracedclauses() {
        return uml_tracedclauses;
    }

    public void addUml_tracedclause(Uml_tracedclause uml_tracedclause) {
        this.uml_tracedclauses.add(uml_tracedclause);
    }
    public uml_TracedOutputPin getUml_tracedoutputpin() {
        return uml_tracedoutputpin;
    }

    public void setUml_tracedoutputpin(uml_TracedOutputPin uml_tracedoutputpin) {
        this.uml_tracedoutputpin = uml_tracedoutputpin;
    }
    public List<uml_TracedOutputPin> getUml_tracedoutputpins() {
        return uml_tracedoutputpins;
    }

    public void addUml_tracedoutputpin(Uml_tracedoutputpin uml_tracedoutputpin) {
        this.uml_tracedoutputpins.add(uml_tracedoutputpin);
    }

}