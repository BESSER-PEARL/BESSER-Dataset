





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_usagemodel_pc_UserData  {






    private UsageModel usagemodel;




    private List<VariableUsage> variableusages;




    private composition_pc_AssemblyContext composition_pc_assemblycontext;


    public pcm_pc_usagemodel_pc_UserData(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_pc_usagemodel_pc_UserData(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
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
    public composition_pc_AssemblyContext getComposition_pc_assemblycontext() {
        return composition_pc_assemblycontext;
    }

    public void setComposition_pc_assemblycontext(composition_pc_AssemblyContext composition_pc_assemblycontext) {
        this.composition_pc_assemblycontext = composition_pc_assemblycontext;
    }

}