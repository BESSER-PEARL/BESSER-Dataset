





import java.util.List;
import java.util.ArrayList;

public class standard_PopulationModelLabel extends DynamicNodeLabel {

    private String populationIdentifier;



    public standard_PopulationModelLabel(
        String populationIdentifier    ) {
        super(
        );
        this.populationIdentifier = populationIdentifier;
    }


    public String getPopulationidentifier() {
        return populationIdentifier;
    }

    public void setPopulationidentifier(String populationIdentifier) {
        this.populationIdentifier = populationIdentifier;
    }


}