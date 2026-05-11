





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FMEA_FMEDAEntry extends FMEAEntry {

    private float diagnosisRate;



    public failureLogic_FMEA_FMEDAEntry(
        float diagnosisRate    ) {
        super(
        );
        this.diagnosisRate = diagnosisRate;
    }


    public float getDiagnosisrate() {
        return diagnosisRate;
    }

    public void setDiagnosisrate(float diagnosisRate) {
        this.diagnosisRate = diagnosisRate;
    }


}