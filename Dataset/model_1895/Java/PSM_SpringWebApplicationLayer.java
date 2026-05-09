





import java.util.List;
import java.util.ArrayList;

public class PSM_SpringWebApplicationLayer extends ArtifactElement {

    private String LayerName;





    private PSM_JavaSpringWebApplicationProject psm_javaspringwebapplicationproject;


    public PSM_SpringWebApplicationLayer(
        String LayerName    ) {
        super(
        );
        this.LayerName = LayerName;
    }


    public String getLayername() {
        return LayerName;
    }

    public void setLayername(String LayerName) {
        this.LayerName = LayerName;
    }

    public PSM_JavaSpringWebApplicationProject getPsm_javaspringwebapplicationproject() {
        return psm_javaspringwebapplicationproject;
    }

    public void setPsm_javaspringwebapplicationproject(PSM_JavaSpringWebApplicationProject psm_javaspringwebapplicationproject) {
        this.psm_javaspringwebapplicationproject = psm_javaspringwebapplicationproject;
    }

}