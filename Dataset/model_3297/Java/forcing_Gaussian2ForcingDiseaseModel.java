





import java.util.List;
import java.util.ArrayList;

public class forcing_Gaussian2ForcingDiseaseModel extends StochasticSIRDiseaseModel {

    private float att2;
    private float att1;
    private float modulationPhaseShift;
    private float sigma2;
    private float att4;
    private float modulationFloor;
    private float att3;
    private float sigma2_2;
    private float modulationPeriod;



    public forcing_Gaussian2ForcingDiseaseModel(
        float att2,        float att1,        float modulationPhaseShift,        float sigma2,        float att4,        float modulationFloor,        float att3,        float sigma2_2,        float modulationPeriod    ) {
        super(
        );
        this.att2 = att2;
        this.att1 = att1;
        this.modulationPhaseShift = modulationPhaseShift;
        this.sigma2 = sigma2;
        this.att4 = att4;
        this.modulationFloor = modulationFloor;
        this.att3 = att3;
        this.sigma2_2 = sigma2_2;
        this.modulationPeriod = modulationPeriod;
    }


    public float getAtt2() {
        return att2;
    }

    public void setAtt2(float att2) {
        this.att2 = att2;
    }
    public float getAtt1() {
        return att1;
    }

    public void setAtt1(float att1) {
        this.att1 = att1;
    }
    public float getModulationphaseshift() {
        return modulationPhaseShift;
    }

    public void setModulationphaseshift(float modulationPhaseShift) {
        this.modulationPhaseShift = modulationPhaseShift;
    }
    public float getSigma2() {
        return sigma2;
    }

    public void setSigma2(float sigma2) {
        this.sigma2 = sigma2;
    }
    public float getAtt4() {
        return att4;
    }

    public void setAtt4(float att4) {
        this.att4 = att4;
    }
    public float getModulationfloor() {
        return modulationFloor;
    }

    public void setModulationfloor(float modulationFloor) {
        this.modulationFloor = modulationFloor;
    }
    public float getAtt3() {
        return att3;
    }

    public void setAtt3(float att3) {
        this.att3 = att3;
    }
    public float getSigma2_2() {
        return sigma2_2;
    }

    public void setSigma2_2(float sigma2_2) {
        this.sigma2_2 = sigma2_2;
    }
    public float getModulationperiod() {
        return modulationPeriod;
    }

    public void setModulationperiod(float modulationPeriod) {
        this.modulationPeriod = modulationPeriod;
    }


}