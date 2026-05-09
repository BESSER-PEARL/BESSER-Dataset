





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ConsiderIgnoreFragment extends CombinedFragment {






    private List<CompleteDSLPckg_NamedElement> completedslpckg_namedelements;


    public CompleteDSLPckg_ConsiderIgnoreFragment(
    ) {
        super(
        );
        this.completedslpckg_namedelements = new ArrayList<>();
    }

    public CompleteDSLPckg_ConsiderIgnoreFragment(
        ArrayList<CompleteDSLPckg_NamedElement> completedslpckg_namedelements    ) {
        this.completedslpckg_namedelements = completedslpckg_namedelements;
    }


    public List<CompleteDSLPckg_NamedElement> getCompletedslpckg_namedelements() {
        return completedslpckg_namedelements;
    }

    public void addCompletedslpckg_namedelement(Completedslpckg_namedelement completedslpckg_namedelement) {
        this.completedslpckg_namedelements.add(completedslpckg_namedelement);
    }

}