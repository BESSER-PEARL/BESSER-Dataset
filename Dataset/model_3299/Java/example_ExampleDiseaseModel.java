





import java.util.List;
import java.util.ArrayList;

public class example_ExampleDiseaseModel extends StochasticSIRDiseaseModel {

    private float modulationPhaseShift;
    private float seasonalModulationExponent;
    private float modulationPeriod;
    private float seasonalModulationFloor;



    public example_ExampleDiseaseModel(
        float modulationPhaseShift,        float seasonalModulationExponent,        float modulationPeriod,        float seasonalModulationFloor    ) {
        super(
        );
        this.modulationPhaseShift = modulationPhaseShift;
        this.seasonalModulationExponent = seasonalModulationExponent;
        this.modulationPeriod = modulationPeriod;
        this.seasonalModulationFloor = seasonalModulationFloor;
    }


    public float getModulationphaseshift() {
        return modulationPhaseShift;
    }

    public void setModulationphaseshift(float modulationPhaseShift) {
        this.modulationPhaseShift = modulationPhaseShift;
    }
    public float getSeasonalmodulationexponent() {
        return seasonalModulationExponent;
    }

    public void setSeasonalmodulationexponent(float seasonalModulationExponent) {
        this.seasonalModulationExponent = seasonalModulationExponent;
    }
    public float getModulationperiod() {
        return modulationPeriod;
    }

    public void setModulationperiod(float modulationPeriod) {
        this.modulationPeriod = modulationPeriod;
    }
    public float getSeasonalmodulationfloor() {
        return seasonalModulationFloor;
    }

    public void setSeasonalmodulationfloor(float seasonalModulationFloor) {
        this.seasonalModulationFloor = seasonalModulationFloor;
    }


}