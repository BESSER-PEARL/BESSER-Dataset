





import java.util.List;
import java.util.ArrayList;

public class dbl_AnnotateableElement  {






    private List<dbl_Annotation> dbl_annotations;


    public dbl_AnnotateableElement(
    ) {
        this.dbl_annotations = new ArrayList<>();
    }

    public dbl_AnnotateableElement(
        ArrayList<dbl_Annotation> dbl_annotations    ) {
        this.dbl_annotations = dbl_annotations;
    }


    public List<dbl_Annotation> getDbl_annotations() {
        return dbl_annotations;
    }

    public void addDbl_annotation(Dbl_annotation dbl_annotation) {
        this.dbl_annotations.add(dbl_annotation);
    }

}