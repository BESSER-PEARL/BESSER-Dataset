





import java.util.List;
import java.util.ArrayList;

public class PSM_JavaAnnotation extends ArtifactElement {

    private String AnnotationName;





    private PSM_JavaElement psm_javaelement;


    public PSM_JavaAnnotation(
        String AnnotationName    ) {
        super(
        );
        this.AnnotationName = AnnotationName;
    }


    public String getAnnotationname() {
        return AnnotationName;
    }

    public void setAnnotationname(String AnnotationName) {
        this.AnnotationName = AnnotationName;
    }

    public PSM_JavaElement getPsm_javaelement() {
        return psm_javaelement;
    }

    public void setPsm_javaelement(PSM_JavaElement psm_javaelement) {
        this.psm_javaelement = psm_javaelement;
    }

}