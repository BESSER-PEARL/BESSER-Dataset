





import java.util.List;
import java.util.ArrayList;

public class pcm_av_usagemodel_av_UserData  {






    private composition_av_AssemblyContext composition_av_assemblycontext;




    private List<VariableUsage> variableusages;




    private UsageModel usagemodel;


    public pcm_av_usagemodel_av_UserData(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_av_usagemodel_av_UserData(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
    }


    public composition_av_AssemblyContext getComposition_av_assemblycontext() {
        return composition_av_assemblycontext;
    }

    public void setComposition_av_assemblycontext(composition_av_AssemblyContext composition_av_assemblycontext) {
        this.composition_av_assemblycontext = composition_av_assemblycontext;
    }
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public UsageModel getUsagemodel() {
        return usagemodel;
    }

    public void setUsagemodel(UsageModel usagemodel) {
        this.usagemodel = usagemodel;
    }

}