





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_PackageCS extends NamedElementCS {






    private List<oclinEcoreCST_ClassifierCS> oclinecorecst_classifiercss;




    private oclinEcoreCST_PackageCS oclinecorecst_packagecs;


    public oclinEcoreCST_PackageCS(
    ) {
        super(
        );
        this.oclinecorecst_classifiercss = new ArrayList<>();
    }

    public oclinEcoreCST_PackageCS(
        ArrayList<oclinEcoreCST_ClassifierCS> oclinecorecst_classifiercss    ) {
        this.oclinecorecst_classifiercss = oclinecorecst_classifiercss;
    }


    public List<oclinEcoreCST_ClassifierCS> getOclinecorecst_classifiercss() {
        return oclinecorecst_classifiercss;
    }

    public void addOclinecorecst_classifiercs(Oclinecorecst_classifiercs oclinecorecst_classifiercs) {
        this.oclinecorecst_classifiercss.add(oclinecorecst_classifiercs);
    }
    public oclinEcoreCST_PackageCS getOclinecorecst_packagecs() {
        return oclinecorecst_packagecs;
    }

    public void setOclinecorecst_packagecs(oclinEcoreCST_PackageCS oclinecorecst_packagecs) {
        this.oclinecorecst_packagecs = oclinecorecst_packagecs;
    }

}