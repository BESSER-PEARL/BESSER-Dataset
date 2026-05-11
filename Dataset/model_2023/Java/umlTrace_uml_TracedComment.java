





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedComment extends TracedElement {






    private List<uml_TracedElement> uml_tracedelements;


    public umlTrace_uml_TracedComment(
    ) {
        super(
        );
        this.uml_tracedelements = new ArrayList<>();
    }

    public umlTrace_uml_TracedComment(
        ArrayList<uml_TracedElement> uml_tracedelements    ) {
        this.uml_tracedelements = uml_tracedelements;
    }


    public List<uml_TracedElement> getUml_tracedelements() {
        return uml_tracedelements;
    }

    public void addUml_tracedelement(Uml_tracedelement uml_tracedelement) {
        this.uml_tracedelements.add(uml_tracedelement);
    }

}