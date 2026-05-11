





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedVertex extends TracedNamedElement {






    private List<uml_TracedTransition> uml_tracedtransitions;




    private List<uml_TracedTransition> uml_tracedtransitions;




    private uml_TracedRegion uml_tracedregion;


    public umlTrace_uml_TracedVertex(
    ) {
        super(
        );
        this.uml_tracedtransitions = new ArrayList<>();
        this.uml_tracedtransitions = new ArrayList<>();
    }

    public umlTrace_uml_TracedVertex(
        ArrayList<uml_TracedTransition> uml_tracedtransitions,        ArrayList<uml_TracedTransition> uml_tracedtransitions    ) {
        this.uml_tracedtransitions = uml_tracedtransitions;
        this.uml_tracedtransitions = uml_tracedtransitions;
    }


    public List<uml_TracedTransition> getUml_tracedtransitions() {
        return uml_tracedtransitions;
    }

    public void addUml_tracedtransition(Uml_tracedtransition uml_tracedtransition) {
        this.uml_tracedtransitions.add(uml_tracedtransition);
    }
    public List<uml_TracedTransition> getUml_tracedtransitions() {
        return uml_tracedtransitions;
    }

    public void addUml_tracedtransition(Uml_tracedtransition uml_tracedtransition) {
        this.uml_tracedtransitions.add(uml_tracedtransition);
    }
    public uml_TracedRegion getUml_tracedregion() {
        return uml_tracedregion;
    }

    public void setUml_tracedregion(uml_TracedRegion uml_tracedregion) {
        this.uml_tracedregion = uml_tracedregion;
    }

}