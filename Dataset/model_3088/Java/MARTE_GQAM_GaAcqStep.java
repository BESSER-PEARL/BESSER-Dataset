





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaAcqStep extends GaStep {

    private String resUnits;





    private GRM_Resource grm_resource;


    public MARTE_GQAM_GaAcqStep(
        String resUnits    ) {
        super(
        );
        this.resUnits = resUnits;
    }


    public String getResunits() {
        return resUnits;
    }

    public void setResunits(String resUnits) {
        this.resUnits = resUnits;
    }

    public GRM_Resource getGrm_resource() {
        return grm_resource;
    }

    public void setGrm_resource(GRM_Resource grm_resource) {
        this.grm_resource = grm_resource;
    }

}