





import java.util.List;
import java.util.ArrayList;

public class dbl_AnnotatableElement  {






    private List<dbl_AnnotationApplication> dbl_annotationapplications;




    private List<dbl_SimpleAnnotation> dbl_simpleannotations;


    public dbl_AnnotatableElement(
    ) {
        this.dbl_annotationapplications = new ArrayList<>();
        this.dbl_simpleannotations = new ArrayList<>();
    }

    public dbl_AnnotatableElement(
        ArrayList<dbl_AnnotationApplication> dbl_annotationapplications,        ArrayList<dbl_SimpleAnnotation> dbl_simpleannotations    ) {
        this.dbl_annotationapplications = dbl_annotationapplications;
        this.dbl_simpleannotations = dbl_simpleannotations;
    }


    public List<dbl_AnnotationApplication> getDbl_annotationapplications() {
        return dbl_annotationapplications;
    }

    public void addDbl_annotationapplication(Dbl_annotationapplication dbl_annotationapplication) {
        this.dbl_annotationapplications.add(dbl_annotationapplication);
    }
    public List<dbl_SimpleAnnotation> getDbl_simpleannotations() {
        return dbl_simpleannotations;
    }

    public void addDbl_simpleannotation(Dbl_simpleannotation dbl_simpleannotation) {
        this.dbl_simpleannotations.add(dbl_simpleannotation);
    }

}