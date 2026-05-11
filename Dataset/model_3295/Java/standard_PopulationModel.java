





import java.util.List;
import java.util.ArrayList;

public class standard_PopulationModel extends Modifiable, NodeDecorator {

    private String targetISOKey;
    private String populationIdentifier;
    private String name;



    public standard_PopulationModel(
        String targetISOKey,        String populationIdentifier,        String name    ) {
        super(
        );
        this.targetISOKey = targetISOKey;
        this.populationIdentifier = populationIdentifier;
        this.name = name;
    }


    public String getTargetisokey() {
        return targetISOKey;
    }

    public void setTargetisokey(String targetISOKey) {
        this.targetISOKey = targetISOKey;
    }
    public String getPopulationidentifier() {
        return populationIdentifier;
    }

    public void setPopulationidentifier(String populationIdentifier) {
        this.populationIdentifier = populationIdentifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}