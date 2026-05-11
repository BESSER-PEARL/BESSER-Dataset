





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction  {






    private List<VariableUsage> variableusages;




    private Signature signature;




    private QoSAnnotations qosannotations;




    private Role role;


    public pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_pc_qosannotations_pc_SpecifiedOutputParameterAbstraction(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
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
    public QoSAnnotations getQosannotations() {
        return qosannotations;
    }

    public void setQosannotations(QoSAnnotations qosannotations) {
        this.qosannotations = qosannotations;
    }
    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }

}