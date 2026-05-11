





import java.util.List;
import java.util.ArrayList;

public class modelDsl_AnnotationGroup extends AnnotationValue {






    private modelDsl_Field modeldsl_field;




    private modelDsl_Package modeldsl_package;




    private modelDsl_Type modeldsl_type;




    private modelDsl_Container modeldsl_container;




    private List<modelDsl_AnnotationInstance> modeldsl_annotationinstances;


    public modelDsl_AnnotationGroup(
    ) {
        super(
        );
        this.modeldsl_annotationinstances = new ArrayList<>();
    }

    public modelDsl_AnnotationGroup(
        ArrayList<modelDsl_AnnotationInstance> modeldsl_annotationinstances    ) {
        this.modeldsl_annotationinstances = modeldsl_annotationinstances;
    }


    public modelDsl_Field getModeldsl_field() {
        return modeldsl_field;
    }

    public void setModeldsl_field(modelDsl_Field modeldsl_field) {
        this.modeldsl_field = modeldsl_field;
    }
    public modelDsl_Package getModeldsl_package() {
        return modeldsl_package;
    }

    public void setModeldsl_package(modelDsl_Package modeldsl_package) {
        this.modeldsl_package = modeldsl_package;
    }
    public modelDsl_Type getModeldsl_type() {
        return modeldsl_type;
    }

    public void setModeldsl_type(modelDsl_Type modeldsl_type) {
        this.modeldsl_type = modeldsl_type;
    }
    public modelDsl_Container getModeldsl_container() {
        return modeldsl_container;
    }

    public void setModeldsl_container(modelDsl_Container modeldsl_container) {
        this.modeldsl_container = modeldsl_container;
    }
    public List<modelDsl_AnnotationInstance> getModeldsl_annotationinstances() {
        return modeldsl_annotationinstances;
    }

    public void addModeldsl_annotationinstance(Modeldsl_annotationinstance modeldsl_annotationinstance) {
        this.modeldsl_annotationinstances.add(modeldsl_annotationinstance);
    }

}