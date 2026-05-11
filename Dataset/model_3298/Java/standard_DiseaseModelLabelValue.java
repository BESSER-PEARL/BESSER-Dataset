





import java.util.List;
import java.util.ArrayList;

public class standard_DiseaseModelLabelValue extends IntegrationLabelValue, LabelValue {

    private float incidence;
    private float diseaseDeaths;
    private float populationCount;



    public standard_DiseaseModelLabelValue(
        float incidence,        float diseaseDeaths,        float populationCount    ) {
        super(
        );
        this.incidence = incidence;
        this.diseaseDeaths = diseaseDeaths;
        this.populationCount = populationCount;
    }


    public float getIncidence() {
        return incidence;
    }

    public void setIncidence(float incidence) {
        this.incidence = incidence;
    }
    public float getDiseasedeaths() {
        return diseaseDeaths;
    }

    public void setDiseasedeaths(float diseaseDeaths) {
        this.diseaseDeaths = diseaseDeaths;
    }
    public float getPopulationcount() {
        return populationCount;
    }

    public void setPopulationcount(float populationCount) {
        this.populationCount = populationCount;
    }


}