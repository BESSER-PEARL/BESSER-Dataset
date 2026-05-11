





import java.util.List;
import java.util.ArrayList;

public class forcing_ForcingDiseaseModel extends StochasticSIRDiseaseModel {

    private float seasonalModulationFloor;
    private float seasonalModulationExponent;
    private float modulationPhaseShift;
    private float modulationPeriod;



    public forcing_ForcingDiseaseModel(
        float seasonalModulationFloor,        float seasonalModulationExponent,        float modulationPhaseShift,        float modulationPeriod    ) {
        super(
        );
        this.seasonalModulationFloor = seasonalModulationFloor;
        this.seasonalModulationExponent = seasonalModulationExponent;
        this.modulationPhaseShift = modulationPhaseShift;
        this.modulationPeriod = modulationPeriod;
    }


    public float getSeasonalmodulationfloor() {
        return seasonalModulationFloor;
    }

    public void setSeasonalmodulationfloor(float seasonalModulationFloor) {
        this.seasonalModulationFloor = seasonalModulationFloor;
    }
    public float getSeasonalmodulationexponent() {
        return seasonalModulationExponent;
    }

    public void setSeasonalmodulationexponent(float seasonalModulationExponent) {
        this.seasonalModulationExponent = seasonalModulationExponent;
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


}