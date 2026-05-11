





import java.util.List;
import java.util.ArrayList;

public class qm_AnnotatedElement extends TaggedElement {






    private List<qm_AnnotationBase> qm_annotationbases;


    public qm_AnnotatedElement(
    ) {
        super(
        );
        this.qm_annotationbases = new ArrayList<>();
    }

    public qm_AnnotatedElement(
        ArrayList<qm_AnnotationBase> qm_annotationbases    ) {
        this.qm_annotationbases = qm_annotationbases;
    }


    public List<qm_AnnotationBase> getQm_annotationbases() {
        return qm_annotationbases;
    }

    public void addQm_annotationbase(Qm_annotationbase qm_annotationbase) {
        this.qm_annotationbases.add(qm_annotationbase);
    }

}