





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_TimeExpression extends ValueSpecification {






    private CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification;




    private List<CompleteDSLPckg_Observation> completedslpckg_observations;


    public CompleteDSLPckg_TimeExpression(
    ) {
        super(
        );
        this.completedslpckg_observations = new ArrayList<>();
    }

    public CompleteDSLPckg_TimeExpression(
        ArrayList<CompleteDSLPckg_Observation> completedslpckg_observations    ) {
        this.completedslpckg_observations = completedslpckg_observations;
    }


    public CompleteDSLPckg_ValueSpecification getCompletedslpckg_valuespecification() {
        return completedslpckg_valuespecification;
    }

    public void setCompletedslpckg_valuespecification(CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification) {
        this.completedslpckg_valuespecification = completedslpckg_valuespecification;
    }
    public List<CompleteDSLPckg_Observation> getCompletedslpckg_observations() {
        return completedslpckg_observations;
    }

    public void addCompletedslpckg_observation(Completedslpckg_observation completedslpckg_observation) {
        this.completedslpckg_observations.add(completedslpckg_observation);
    }

}