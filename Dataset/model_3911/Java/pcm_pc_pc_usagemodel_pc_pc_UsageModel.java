





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_usagemodel_pc_pc_UsageModel  {






    private List<UsageScenario> usagescenarios;


    public pcm_pc_pc_usagemodel_pc_pc_UsageModel(
    ) {
        this.usagescenarios = new ArrayList<>();
    }

    public pcm_pc_pc_usagemodel_pc_pc_UsageModel(
        ArrayList<UsageScenario> usagescenarios    ) {
        this.usagescenarios = usagescenarios;
    }


    public List<UsageScenario> getUsagescenarios() {
        return usagescenarios;
    }

    public void addUsagescenario(Usagescenario usagescenario) {
        this.usagescenarios.add(usagescenario);
    }

}