





import java.util.List;
import java.util.ArrayList;

public class standard_PopulationGroup  {

    private float fraction;
    private String identifier;





    private standard_DemographicPopulationModel standard_demographicpopulationmodel;


    public standard_PopulationGroup(
        float fraction,        String identifier    ) {
        this.fraction = fraction;
        this.identifier = identifier;
    }


    public float getFraction() {
        return fraction;
    }

    public void setFraction(float fraction) {
        this.fraction = fraction;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public standard_DemographicPopulationModel getStandard_demographicpopulationmodel() {
        return standard_demographicpopulationmodel;
    }

    public void setStandard_demographicpopulationmodel(standard_DemographicPopulationModel standard_demographicpopulationmodel) {
        this.standard_demographicpopulationmodel = standard_demographicpopulationmodel;
    }

}