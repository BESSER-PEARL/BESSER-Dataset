





import java.util.List;
import java.util.ArrayList;

public class pcm_usagemodel_EntryLevelSystemCall extends AbstractUserAction {






    private ProvidedRole providedrole;




    private List<VariableUsage> variableusages;




    private Signature signature;




    private List<VariableUsage> variableusages;


    public pcm_usagemodel_EntryLevelSystemCall(
    ) {
        super(
        );
        this.variableusages = new ArrayList<>();
        this.variableusages = new ArrayList<>();
    }

    public pcm_usagemodel_EntryLevelSystemCall(
        ArrayList<VariableUsage> variableusages,        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
        this.variableusages = variableusages;
    }


    public ProvidedRole getProvidedrole() {
        return providedrole;
    }

    public void setProvidedrole(ProvidedRole providedrole) {
        this.providedrole = providedrole;
    }
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }

}