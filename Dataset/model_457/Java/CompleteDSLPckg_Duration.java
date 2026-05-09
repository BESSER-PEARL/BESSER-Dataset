





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Duration extends ValueSpecification {






    private List<CompleteDSLPckg_Observation> completedslpckg_observations;




    private CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification;


    public CompleteDSLPckg_Duration(
    ) {
        super(
        );
        this.completedslpckg_observations = new ArrayList<>();
    }

    public CompleteDSLPckg_Duration(
        ArrayList<CompleteDSLPckg_Observation> completedslpckg_observations    ) {
        this.completedslpckg_observations = completedslpckg_observations;
    }


    public List<CompleteDSLPckg_Observation> getCompletedslpckg_observations() {
        return completedslpckg_observations;
    }

    public void addCompletedslpckg_observation(Completedslpckg_observation completedslpckg_observation) {
        this.completedslpckg_observations.add(completedslpckg_observation);
    }
    public CompleteDSLPckg_ValueSpecification getCompletedslpckg_valuespecification() {
        return completedslpckg_valuespecification;
    }

    public void setCompletedslpckg_valuespecification(CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification) {
        this.completedslpckg_valuespecification = completedslpckg_valuespecification;
    }

}