





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaAnnotationParameter extends ArtifactElement {

    private String ParameterValue;
    private String ParameterName;





    private PSM_JavaAnnotation psm_javaannotation;


    public PSM_JavaAnnotationParameter(
        String ParameterValue,        String ParameterName    ) {
        super(
        );
        this.ParameterValue = ParameterValue;
        this.ParameterName = ParameterName;
    }


    public String getParametervalue() {
        return ParameterValue;
    }

    public void setParametervalue(String ParameterValue) {
        this.ParameterValue = ParameterValue;
    }
    public String getParametername() {
        return ParameterName;
    }

    public void setParametername(String ParameterName) {
        this.ParameterName = ParameterName;
    }

    public PSM_JavaAnnotation getPsm_javaannotation() {
        return psm_javaannotation;
    }

    public void setPsm_javaannotation(PSM_JavaAnnotation psm_javaannotation) {
        this.psm_javaannotation = psm_javaannotation;
    }

}