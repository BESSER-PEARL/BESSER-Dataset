





import java.util.List;
import java.util.ArrayList;

public class forcing_Gaussian3ForcingDiseaseModel extends Gaussian2ForcingDiseaseModel {

    private float transmissionRate3;
    private float transmissionRate2;
    private float sigma2_3;
    private float modulationFloor_2;



    public forcing_Gaussian3ForcingDiseaseModel(
        float transmissionRate3,        float transmissionRate2,        float sigma2_3,        float modulationFloor_2    ) {
        super(
        );
        this.transmissionRate3 = transmissionRate3;
        this.transmissionRate2 = transmissionRate2;
        this.sigma2_3 = sigma2_3;
        this.modulationFloor_2 = modulationFloor_2;
    }


    public float getTransmissionrate3() {
        return transmissionRate3;
    }

    public void setTransmissionrate3(float transmissionRate3) {
        this.transmissionRate3 = transmissionRate3;
    }
    public float getTransmissionrate2() {
        return transmissionRate2;
    }

    public void setTransmissionrate2(float transmissionRate2) {
        this.transmissionRate2 = transmissionRate2;
    }
    public float getSigma2_3() {
        return sigma2_3;
    }

    public void setSigma2_3(float sigma2_3) {
        this.sigma2_3 = sigma2_3;
    }
    public float getModulationfloor_2() {
        return modulationFloor_2;
    }

    public void setModulationfloor_2(float modulationFloor_2) {
        this.modulationFloor_2 = modulationFloor_2;
    }


}