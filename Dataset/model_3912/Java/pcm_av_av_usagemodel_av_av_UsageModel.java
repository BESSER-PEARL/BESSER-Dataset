





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_usagemodel_av_av_UsageModel  {






    private List<UsageScenario> usagescenarios;


    public pcm_av_av_usagemodel_av_av_UsageModel(
    ) {
        this.usagescenarios = new ArrayList<>();
    }

    public pcm_av_av_usagemodel_av_av_UsageModel(
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