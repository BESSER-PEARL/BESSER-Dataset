





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ConsiderIgnoreFragment extends CombinedFragment {






    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;


    public uml3_0_0_ConsiderIgnoreFragment(
    ) {
        super(
        );
        this.uml3_0_0_namedelements = new ArrayList<>();
    }

    public uml3_0_0_ConsiderIgnoreFragment(
        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements    ) {
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
    }


    public List<uml3_0_0_NamedElement> getUml3_0_0_namedelements() {
        return uml3_0_0_namedelements;
    }

    public void addUml3_0_0_namedelement(Uml3_0_0_namedelement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelements.add(uml3_0_0_namedelement);
    }

}