





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_DocumentCS  {






    private List<oclinEcoreCST_PackageCS> oclinecorecst_packagecss;


    public oclinEcoreCST_DocumentCS(
    ) {
        this.oclinecorecst_packagecss = new ArrayList<>();
    }

    public oclinEcoreCST_DocumentCS(
        ArrayList<oclinEcoreCST_PackageCS> oclinecorecst_packagecss    ) {
        this.oclinecorecst_packagecss = oclinecorecst_packagecss;
    }


    public List<oclinEcoreCST_PackageCS> getOclinecorecst_packagecss() {
        return oclinecorecst_packagecss;
    }

    public void addOclinecorecst_packagecs(Oclinecorecst_packagecs oclinecorecst_packagecs) {
        this.oclinecorecst_packagecss.add(oclinecorecst_packagecs);
    }

}