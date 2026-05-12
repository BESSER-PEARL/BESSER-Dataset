





import java.util.List;
import java.util.ArrayList;

public class UML2_InteractionFragment extends NamedElement {






    private UML2_Lifeline uml2_lifeline;




    private List<UML2_Lifeline> uml2_lifelines;




    private List<UML2_GeneralOrdering> uml2_generalorderings;


    public UML2_InteractionFragment(
    ) {
        super(
        );
        this.uml2_lifelines = new ArrayList<>();
        this.uml2_generalorderings = new ArrayList<>();
    }

    public UML2_InteractionFragment(
        ArrayList<UML2_Lifeline> uml2_lifelines,        ArrayList<UML2_GeneralOrdering> uml2_generalorderings    ) {
        this.uml2_lifelines = uml2_lifelines;
        this.uml2_generalorderings = uml2_generalorderings;
    }


    public UML2_Lifeline getUml2_lifeline() {
        return uml2_lifeline;
    }

    public void setUml2_lifeline(UML2_Lifeline uml2_lifeline) {
        this.uml2_lifeline = uml2_lifeline;
    }
    public List<UML2_Lifeline> getUml2_lifelines() {
        return uml2_lifelines;
    }

    public void addUml2_lifeline(Uml2_lifeline uml2_lifeline) {
        this.uml2_lifelines.add(uml2_lifeline);
    }
    public List<UML2_GeneralOrdering> getUml2_generalorderings() {
        return uml2_generalorderings;
    }

    public void addUml2_generalordering(Uml2_generalordering uml2_generalordering) {
        this.uml2_generalorderings.add(uml2_generalordering);
    }

}