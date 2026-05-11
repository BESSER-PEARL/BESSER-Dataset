





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall extends AbstractUserAction {

    private int priority;





    private List<VariableUsage> variableusages;




    private List<VariableUsage> variableusages;




    private OperationProvidedRole operationprovidedrole;


    public pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall(
        int priority    ) {
        super(
        );
        this.priority = priority;
        this.variableusages = new ArrayList<>();
        this.variableusages = new ArrayList<>();
    }

    public pcm_pc_av_usagemodel_pc_av_EntryLevelSystemCall(
        int priority        ArrayList<VariableUsage> variableusages,        ArrayList<VariableUsage> variableusages    ) {
        this.priority = priority;
        this.variableusages = variableusages;
        this.variableusages = variableusages;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public OperationProvidedRole getOperationprovidedrole() {
        return operationprovidedrole;
    }

    public void setOperationprovidedrole(OperationProvidedRole operationprovidedrole) {
        this.operationprovidedrole = operationprovidedrole;
    }

}