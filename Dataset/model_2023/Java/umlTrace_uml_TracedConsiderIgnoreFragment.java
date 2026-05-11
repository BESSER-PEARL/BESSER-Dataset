





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedConsiderIgnoreFragment extends TracedCombinedFragment {






    private List<uml_TracedNamedElement> uml_tracednamedelements;


    public umlTrace_uml_TracedConsiderIgnoreFragment(
    ) {
        super(
        );
        this.uml_tracednamedelements = new ArrayList<>();
    }

    public umlTrace_uml_TracedConsiderIgnoreFragment(
        ArrayList<uml_TracedNamedElement> uml_tracednamedelements    ) {
        this.uml_tracednamedelements = uml_tracednamedelements;
    }


    public List<uml_TracedNamedElement> getUml_tracednamedelements() {
        return uml_tracednamedelements;
    }

    public void addUml_tracednamedelement(Uml_tracednamedelement uml_tracednamedelement) {
        this.uml_tracednamedelements.add(uml_tracednamedelement);
    }

}