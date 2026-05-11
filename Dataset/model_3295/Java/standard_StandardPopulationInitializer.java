





import java.util.List;
import java.util.ArrayList;

public class standard_StandardPopulationInitializer extends PopulationInitializer {

    private float individuals;
    private boolean useDensity;



    public standard_StandardPopulationInitializer(
        float individuals,        boolean useDensity    ) {
        super(
        );
        this.individuals = individuals;
        this.useDensity = useDensity;
    }


    public float getIndividuals() {
        return individuals;
    }

    public void setIndividuals(float individuals) {
        this.individuals = individuals;
    }
    public boolean getUsedensity() {
        return useDensity;
    }

    public void setUsedensity(boolean useDensity) {
        this.useDensity = useDensity;
    }


}