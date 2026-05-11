





import java.util.List;
import java.util.ArrayList;

public class pcm_seff_ExternalCallAction extends AbstractAction {






    private Signature signature;




    private List<VariableUsage> variableusages;




    private List<VariableUsage> variableusages;




    private Role role;


    public pcm_seff_ExternalCallAction(
    ) {
        super(
        );
        this.variableusages = new ArrayList<>();
        this.variableusages = new ArrayList<>();
    }

    public pcm_seff_ExternalCallAction(
        ArrayList<VariableUsage> variableusages,        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
        this.variableusages = variableusages;
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
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }

}