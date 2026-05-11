





import java.util.List;
import java.util.ArrayList;

public class odemcustom_AnnotatableElement  {






    private List<odemcustom_SimpleAnnotation> odemcustom_simpleannotations;




    private List<odemcustom_AnnotationApplication> odemcustom_annotationapplications;


    public odemcustom_AnnotatableElement(
    ) {
        this.odemcustom_simpleannotations = new ArrayList<>();
        this.odemcustom_annotationapplications = new ArrayList<>();
    }

    public odemcustom_AnnotatableElement(
        ArrayList<odemcustom_SimpleAnnotation> odemcustom_simpleannotations,        ArrayList<odemcustom_AnnotationApplication> odemcustom_annotationapplications    ) {
        this.odemcustom_simpleannotations = odemcustom_simpleannotations;
        this.odemcustom_annotationapplications = odemcustom_annotationapplications;
    }


    public List<odemcustom_SimpleAnnotation> getOdemcustom_simpleannotations() {
        return odemcustom_simpleannotations;
    }

    public void addOdemcustom_simpleannotation(Odemcustom_simpleannotation odemcustom_simpleannotation) {
        this.odemcustom_simpleannotations.add(odemcustom_simpleannotation);
    }
    public List<odemcustom_AnnotationApplication> getOdemcustom_annotationapplications() {
        return odemcustom_annotationapplications;
    }

    public void addOdemcustom_annotationapplication(Odemcustom_annotationapplication odemcustom_annotationapplication) {
        this.odemcustom_annotationapplications.add(odemcustom_annotationapplication);
    }

}