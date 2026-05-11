





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_usagemodel_av_av_UserData  {






    private UsageModel usagemodel;




    private List<VariableUsage> variableusages;




    private composition_av_av_AssemblyContext composition_av_av_assemblycontext;


    public pcm_av_av_usagemodel_av_av_UserData(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_av_av_usagemodel_av_av_UserData(
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
    public composition_av_av_AssemblyContext getComposition_av_av_assemblycontext() {
        return composition_av_av_assemblycontext;
    }

    public void setComposition_av_av_assemblycontext(composition_av_av_AssemblyContext composition_av_av_assemblycontext) {
        this.composition_av_av_assemblycontext = composition_av_av_assemblycontext;
    }

}