





import java.util.List;
import java.util.ArrayList;

public class standard_DiseaseModel extends SanityChecker, NodeDecorator, Modifiable {

    private String diseaseName;
    private float backgroundMortalityRate;
    private float relativeTolerance;
    private boolean finiteDifference;
    private float backgroundBirthRate;
    private boolean frequencyDependent;
    private String timePeriod;
    private String populationIdentifier;



    public standard_DiseaseModel(
        String diseaseName,        float backgroundMortalityRate,        float relativeTolerance,        boolean finiteDifference,        float backgroundBirthRate,        boolean frequencyDependent,        String timePeriod,        String populationIdentifier    ) {
        super(
        );
        this.diseaseName = diseaseName;
        this.backgroundMortalityRate = backgroundMortalityRate;
        this.relativeTolerance = relativeTolerance;
        this.finiteDifference = finiteDifference;
        this.backgroundBirthRate = backgroundBirthRate;
        this.frequencyDependent = frequencyDependent;
        this.timePeriod = timePeriod;
        this.populationIdentifier = populationIdentifier;
    }


    public String getDiseasename() {
        return diseaseName;
    }

    public void setDiseasename(String diseaseName) {
        this.diseaseName = diseaseName;
    }
    public float getBackgroundmortalityrate() {
        return backgroundMortalityRate;
    }

    public void setBackgroundmortalityrate(float backgroundMortalityRate) {
        this.backgroundMortalityRate = backgroundMortalityRate;
    }
    public float getRelativetolerance() {
        return relativeTolerance;
    }

    public void setRelativetolerance(float relativeTolerance) {
        this.relativeTolerance = relativeTolerance;
    }
    public boolean getFinitedifference() {
        return finiteDifference;
    }

    public void setFinitedifference(boolean finiteDifference) {
        this.finiteDifference = finiteDifference;
    }
    public float getBackgroundbirthrate() {
        return backgroundBirthRate;
    }

    public void setBackgroundbirthrate(float backgroundBirthRate) {
        this.backgroundBirthRate = backgroundBirthRate;
    }
    public boolean getFrequencydependent() {
        return frequencyDependent;
    }

    public void setFrequencydependent(boolean frequencyDependent) {
        this.frequencyDependent = frequencyDependent;
    }
    public String getTimeperiod() {
        return timePeriod;
    }

    public void setTimeperiod(String timePeriod) {
        this.timePeriod = timePeriod;
    }
    public String getPopulationidentifier() {
        return populationIdentifier;
    }

    public void setPopulationidentifier(String populationIdentifier) {
        this.populationIdentifier = populationIdentifier;
    }


}