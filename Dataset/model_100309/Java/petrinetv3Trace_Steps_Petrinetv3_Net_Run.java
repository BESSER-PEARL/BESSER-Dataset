





import java.util.List;
import java.util.ArrayList;

public class petrinetv3Trace_Steps_Petrinetv3_Net_Run extends BigStep {






    private List<Petrinetv3_Net_Run_AbstractSubStep> petrinetv3_net_run_abstractsubsteps;


    public petrinetv3Trace_Steps_Petrinetv3_Net_Run(
    ) {
        super(
        );
        this.petrinetv3_net_run_abstractsubsteps = new ArrayList<>();
    }

    public petrinetv3Trace_Steps_Petrinetv3_Net_Run(
        ArrayList<Petrinetv3_Net_Run_AbstractSubStep> petrinetv3_net_run_abstractsubsteps    ) {
        this.petrinetv3_net_run_abstractsubsteps = petrinetv3_net_run_abstractsubsteps;
    }


    public List<Petrinetv3_Net_Run_AbstractSubStep> getPetrinetv3_net_run_abstractsubsteps() {
        return petrinetv3_net_run_abstractsubsteps;
    }

    public void addPetrinetv3_net_run_abstractsubstep(Petrinetv3_net_run_abstractsubstep petrinetv3_net_run_abstractsubstep) {
        this.petrinetv3_net_run_abstractsubsteps.add(petrinetv3_net_run_abstractsubstep);
    }

}