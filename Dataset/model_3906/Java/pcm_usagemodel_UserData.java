





import java.util.List;
import java.util.ArrayList;

public class pcm_usagemodel_UserData  {






    private List<VariableUsage> variableusages;




    private composition_AssemblyContext composition_assemblycontext;


    public pcm_usagemodel_UserData(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_usagemodel_UserData(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
    }


    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public composition_AssemblyContext getComposition_assemblycontext() {
        return composition_assemblycontext;
    }

    public void setComposition_assemblycontext(composition_AssemblyContext composition_assemblycontext) {
        this.composition_assemblycontext = composition_assemblycontext;
    }

}