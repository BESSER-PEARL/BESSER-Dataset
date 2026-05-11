





import java.util.List;
import java.util.ArrayList;

public class CommonBehavior_SimpleTime_Duration extends ValueSpecification {






    private List<Observation> observations;


    public CommonBehavior_SimpleTime_Duration(
    ) {
        super(
        );
        this.observations = new ArrayList<>();
    }

    public CommonBehavior_SimpleTime_Duration(
        ArrayList<Observation> observations    ) {
        this.observations = observations;
    }


    public List<Observation> getObservations() {
        return observations;
    }

    public void addObservation(Observation observation) {
        this.observations.add(observation);
    }

}