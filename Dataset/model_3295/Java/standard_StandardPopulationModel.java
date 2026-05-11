





import java.util.List;
import java.util.ArrayList;

public class standard_StandardPopulationModel extends PopulationModel, IntegrationDecorator {

    private String timePeriod;
    private float birthRate;
    private float deathRate;



    public standard_StandardPopulationModel(
        String timePeriod,        float birthRate,        float deathRate    ) {
        super(
        );
        this.timePeriod = timePeriod;
        this.birthRate = birthRate;
        this.deathRate = deathRate;
    }


    public String getTimeperiod() {
        return timePeriod;
    }

    public void setTimeperiod(String timePeriod) {
        this.timePeriod = timePeriod;
    }
    public float getBirthrate() {
        return birthRate;
    }

    public void setBirthrate(float birthRate) {
        this.birthRate = birthRate;
    }
    public float getDeathrate() {
        return deathRate;
    }

    public void setDeathrate(float deathRate) {
        this.deathRate = deathRate;
    }


}