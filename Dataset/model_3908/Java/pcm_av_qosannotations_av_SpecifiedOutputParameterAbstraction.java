





import java.util.List;
import java.util.ArrayList;

public class pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction  {






    private Role role;




    private Signature signature;




    private QoSAnnotations qosannotations;




    private List<VariableUsage> variableusages;


    public pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_av_qosannotations_av_SpecifiedOutputParameterAbstraction(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
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
    public QoSAnnotations getQosannotations() {
        return qosannotations;
    }

    public void setQosannotations(QoSAnnotations qosannotations) {
        this.qosannotations = qosannotations;
    }
    public List<VariableUsage> getVariableusages() {
        return variableusages;
    }

    public void addVariableusage(Variableusage variableusage) {
        this.variableusages.add(variableusage);
    }

}