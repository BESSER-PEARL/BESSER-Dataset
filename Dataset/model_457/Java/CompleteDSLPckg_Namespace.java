





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Namespace extends NamedElement {






    private List<CompleteDSLPckg_PackageableElement> completedslpckg_packageableelements;


    public CompleteDSLPckg_Namespace(
    ) {
        super(
        );
        this.completedslpckg_packageableelements = new ArrayList<>();
    }

    public CompleteDSLPckg_Namespace(
        ArrayList<CompleteDSLPckg_PackageableElement> completedslpckg_packageableelements    ) {
        this.completedslpckg_packageableelements = completedslpckg_packageableelements;
    }


    public List<CompleteDSLPckg_PackageableElement> getCompletedslpckg_packageableelements() {
        return completedslpckg_packageableelements;
    }

    public void addCompletedslpckg_packageableelement(Completedslpckg_packageableelement completedslpckg_packageableelement) {
        this.completedslpckg_packageableelements.add(completedslpckg_packageableelement);
    }

}