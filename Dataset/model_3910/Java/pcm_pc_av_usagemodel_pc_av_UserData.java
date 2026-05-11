





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_usagemodel_pc_av_UserData  {






    private composition_pc_av_AssemblyContext composition_pc_av_assemblycontext;




    private UsageModel usagemodel;




    private List<VariableUsage> variableusages;


    public pcm_pc_av_usagemodel_pc_av_UserData(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_pc_av_usagemodel_pc_av_UserData(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
    }


    public composition_pc_av_AssemblyContext getComposition_pc_av_assemblycontext() {
        return composition_pc_av_assemblycontext;
    }

    public void setComposition_pc_av_assemblycontext(composition_pc_av_AssemblyContext composition_pc_av_assemblycontext) {
        this.composition_pc_av_assemblycontext = composition_pc_av_assemblycontext;
    }
    public UsageModel getUsagemodel() {
        return usagemodel;
    }

    public void setUsagemodel(UsageModel usagemodel) {
        this.usagemodel = usagemodel;
    }
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }

}