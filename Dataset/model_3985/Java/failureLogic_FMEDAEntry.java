





import java.util.List;
import java.util.ArrayList;

public class failureLogic_FMEDAEntry extends FMEAEntry {

    private float diagnosisRate;





    private failureLogic_ProbDist failurelogic_probdist;


    public failureLogic_FMEDAEntry(
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

    public failureLogic_ProbDist getFailurelogic_probdist() {
        return failurelogic_probdist;
    }

    public void setFailurelogic_probdist(failureLogic_ProbDist failurelogic_probdist) {
        this.failurelogic_probdist = failurelogic_probdist;
    }

}