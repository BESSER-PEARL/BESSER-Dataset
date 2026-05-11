





import java.util.List;
import java.util.ArrayList;

public class pcm_qosannotations_SpecifiedOutputParameterAbstraction  {






    private List<VariableUsage> variableusages;




    private Role role;




    private Signature signature;


    public pcm_qosannotations_SpecifiedOutputParameterAbstraction(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_qosannotations_SpecifiedOutputParameterAbstraction(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
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
    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }

}