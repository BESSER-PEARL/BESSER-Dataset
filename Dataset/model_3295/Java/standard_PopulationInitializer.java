





import java.util.List;
import java.util.ArrayList;

public class standard_PopulationInitializer extends Modifiable, NodeDecorator {

    private String populationIdentifier;
    private String targetISOKey;



    public standard_PopulationInitializer(
        String populationIdentifier,        String targetISOKey    ) {
        super(
        );
        this.populationIdentifier = populationIdentifier;
        this.targetISOKey = targetISOKey;
    }


    public String getPopulationidentifier() {
        return populationIdentifier;
    }

    public void setPopulationidentifier(String populationIdentifier) {
        this.populationIdentifier = populationIdentifier;
    }
    public String getTargetisokey() {
        return targetISOKey;
    }

    public void setTargetisokey(String targetISOKey) {
        this.targetISOKey = targetISOKey;
    }


}