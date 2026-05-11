





import java.util.List;
import java.util.ArrayList;

public class modelDsl_Annotation extends Element {






    private List<modelDsl_AnnotationInstance> modeldsl_annotationinstances;




    private modelDsl_AnnotationInstance modeldsl_annotationinstance;


    public modelDsl_Annotation(
    ) {
        super(
        );
        this.modeldsl_annotationinstances = new ArrayList<>();
    }

    public modelDsl_Annotation(
        ArrayList<modelDsl_AnnotationInstance> modeldsl_annotationinstances    ) {
        this.modeldsl_annotationinstances = modeldsl_annotationinstances;
    }


    public List<modelDsl_AnnotationInstance> getModeldsl_annotationinstances() {
        return modeldsl_annotationinstances;
    }

    public void addModeldsl_annotationinstance(Modeldsl_annotationinstance modeldsl_annotationinstance) {
        this.modeldsl_annotationinstances.add(modeldsl_annotationinstance);
    }
    public modelDsl_AnnotationInstance getModeldsl_annotationinstance() {
        return modeldsl_annotationinstance;
    }

    public void setModeldsl_annotationinstance(modelDsl_AnnotationInstance modeldsl_annotationinstance) {
        this.modeldsl_annotationinstance = modeldsl_annotationinstance;
    }

}