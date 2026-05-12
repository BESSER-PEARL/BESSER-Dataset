





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_ParallelStep extends Step {






    private List<UseCaseDSL_ParallelFlow> usecasedsl_parallelflows;


    public UseCaseDSL_ParallelStep(
    ) {
        super(
        );
        this.usecasedsl_parallelflows = new ArrayList<>();
    }

    public UseCaseDSL_ParallelStep(
        ArrayList<UseCaseDSL_ParallelFlow> usecasedsl_parallelflows    ) {
        this.usecasedsl_parallelflows = usecasedsl_parallelflows;
    }


    public List<UseCaseDSL_ParallelFlow> getUsecasedsl_parallelflows() {
        return usecasedsl_parallelflows;
    }

    public void addUsecasedsl_parallelflow(Usecasedsl_parallelflow usecasedsl_parallelflow) {
        this.usecasedsl_parallelflows.add(usecasedsl_parallelflow);
    }

}