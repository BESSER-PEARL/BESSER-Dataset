





import java.util.List;
import java.util.ArrayList;

public class dbl_AnnotationApplication  {






    private dbl_Annotation dbl_annotation;




    private List<dbl_KeyValuePair> dbl_keyvaluepairs;




    private dbl_AnnotatableElement dbl_annotatableelement;


    public dbl_AnnotationApplication(
    ) {
        this.dbl_keyvaluepairs = new ArrayList<>();
    }

    public dbl_AnnotationApplication(
        ArrayList<dbl_KeyValuePair> dbl_keyvaluepairs    ) {
        this.dbl_keyvaluepairs = dbl_keyvaluepairs;
    }


    public dbl_Annotation getDbl_annotation() {
        return dbl_annotation;
    }

    public void setDbl_annotation(dbl_Annotation dbl_annotation) {
        this.dbl_annotation = dbl_annotation;
    }
    public List<dbl_KeyValuePair> getDbl_keyvaluepairs() {
        return dbl_keyvaluepairs;
    }

    public void addDbl_keyvaluepair(Dbl_keyvaluepair dbl_keyvaluepair) {
        this.dbl_keyvaluepairs.add(dbl_keyvaluepair);
    }
    public dbl_AnnotatableElement getDbl_annotatableelement() {
        return dbl_annotatableelement;
    }

    public void setDbl_annotatableelement(dbl_AnnotatableElement dbl_annotatableelement) {
        this.dbl_annotatableelement = dbl_annotatableelement;
    }

}