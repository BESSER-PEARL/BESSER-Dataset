





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction  {






    private Signature signature;




    private Role role;




    private List<VariableUsage> variableusages;




    private QoSAnnotations qosannotations;


    public pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_av_pc_qosannotations_av_pc_SpecifiedOutputParameterAbstraction(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
    }


    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }
    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }
    public QoSAnnotations getQosannotations() {
        return qosannotations;
    }

    public void setQosannotations(QoSAnnotations qosannotations) {
        this.qosannotations = qosannotations;
    }

}