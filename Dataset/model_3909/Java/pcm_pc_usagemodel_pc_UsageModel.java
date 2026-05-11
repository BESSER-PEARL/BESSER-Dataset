





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_usagemodel_pc_UsageModel  {






    private List<UserData> userdatas;




    private List<UsageScenario> usagescenarios;


    public pcm_pc_usagemodel_pc_UsageModel(
    ) {
        this.userdatas = new ArrayList<>();
        this.usagescenarios = new ArrayList<>();
    }

    public pcm_pc_usagemodel_pc_UsageModel(
        ArrayList<UserData> userdatas,        ArrayList<UsageScenario> usagescenarios    ) {
        this.userdatas = userdatas;
        this.usagescenarios = usagescenarios;
    }


    public List<UserData> getUserdatas() {
        return userdatas;
    }

    public void addUserdata(Userdata userdata) {
        this.userdatas.add(userdata);
    }
    public List<UsageScenario> getUsagescenarios() {
        return usagescenarios;
    }

    public void addUsagescenario(Usagescenario usagescenario) {
        this.usagescenarios.add(usagescenario);
    }

}