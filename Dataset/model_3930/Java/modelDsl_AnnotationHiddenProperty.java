





import java.util.List;
import java.util.ArrayList;

public class modelDsl_AnnotationHiddenProperty  {






    private List<modelDsl_AnnotationValue> modeldsl_annotationvalues;




    private modelDsl_AnnotationInstance modeldsl_annotationinstance;




    private modelDsl_AnnotationProperty modeldsl_annotationproperty;


    public modelDsl_AnnotationHiddenProperty(
    ) {
        this.modeldsl_annotationvalues = new ArrayList<>();
    }

    public modelDsl_AnnotationHiddenProperty(
        ArrayList<modelDsl_AnnotationValue> modeldsl_annotationvalues    ) {
        this.modeldsl_annotationvalues = modeldsl_annotationvalues;
    }


    public List<modelDsl_AnnotationValue> getModeldsl_annotationvalues() {
        return modeldsl_annotationvalues;
    }

    public void addModeldsl_annotationvalue(Modeldsl_annotationvalue modeldsl_annotationvalue) {
        this.modeldsl_annotationvalues.add(modeldsl_annotationvalue);
    }
    public modelDsl_AnnotationInstance getModeldsl_annotationinstance() {
        return modeldsl_annotationinstance;
    }

    public void setModeldsl_annotationinstance(modelDsl_AnnotationInstance modeldsl_annotationinstance) {
        this.modeldsl_annotationinstance = modeldsl_annotationinstance;
    }
    public modelDsl_AnnotationProperty getModeldsl_annotationproperty() {
        return modeldsl_annotationproperty;
    }

    public void setModeldsl_annotationproperty(modelDsl_AnnotationProperty modeldsl_annotationproperty) {
        this.modeldsl_annotationproperty = modeldsl_annotationproperty;
    }

}