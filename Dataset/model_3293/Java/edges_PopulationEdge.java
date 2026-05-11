





import java.util.List;
import java.util.ArrayList;

public class edges_PopulationEdge extends Edge {

    private String populationIdentifier;



    public edges_PopulationEdge(
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