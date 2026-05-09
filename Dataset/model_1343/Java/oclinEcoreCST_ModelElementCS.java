





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_ModelElementCS  {






    private List<oclinEcoreCST_AnnotationCS> oclinecorecst_annotationcss;


    public oclinEcoreCST_ModelElementCS(
    ) {
        this.oclinecorecst_annotationcss = new ArrayList<>();
    }

    public oclinEcoreCST_ModelElementCS(
        ArrayList<oclinEcoreCST_AnnotationCS> oclinecorecst_annotationcss    ) {
        this.oclinecorecst_annotationcss = oclinecorecst_annotationcss;
    }


    public List<oclinEcoreCST_AnnotationCS> getOclinecorecst_annotationcss() {
        return oclinecorecst_annotationcss;
    }

    public void addOclinecorecst_annotationcs(Oclinecorecst_annotationcs oclinecorecst_annotationcs) {
        this.oclinecorecst_annotationcss.add(oclinecorecst_annotationcs);
    }

}