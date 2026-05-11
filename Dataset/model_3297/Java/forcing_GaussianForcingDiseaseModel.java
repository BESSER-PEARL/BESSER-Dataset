





import java.util.List;
import java.util.ArrayList;

public class forcing_GaussianForcingDiseaseModel extends StochasticSIRDiseaseModel {

    private float modulationPhaseShift;
    private float modulationPeriod;
    private float sigma2;
    private float modulationFloor;



    public forcing_GaussianForcingDiseaseModel(
        float modulationPhaseShift,        float modulationPeriod,        float sigma2,        float modulationFloor    ) {
        super(
        );
        this.modulationPhaseShift = modulationPhaseShift;
        this.modulationPeriod = modulationPeriod;
        this.sigma2 = sigma2;
        this.modulationFloor = modulationFloor;
    }


    public float getModulationphaseshift() {
        return modulationPhaseShift;
    }

    public void setModulationphaseshift(float modulationPhaseShift) {
        this.modulationPhaseShift = modulationPhaseShift;
    }
    public float getModulationperiod() {
        return modulationPeriod;
    }

    public void setModulationperiod(float modulationPeriod) {
        this.modulationPeriod = modulationPeriod;
    }
    public float getSigma2() {
        return sigma2;
    }

    public void setSigma2(float sigma2) {
        this.sigma2 = sigma2;
    }
    public float getModulationfloor() {
        return modulationFloor;
    }

    public void setModulationfloor(float modulationFloor) {
        this.modulationFloor = modulationFloor;
    }


}