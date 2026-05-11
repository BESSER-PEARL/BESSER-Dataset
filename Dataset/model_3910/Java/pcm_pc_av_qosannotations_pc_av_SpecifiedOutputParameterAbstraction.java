





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction  {






    private Role role;




    private List<VariableUsage> variableusages;


    public pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction(
    ) {
        this.variableusages = new ArrayList<>();
    }

    public pcm_pc_av_qosannotations_pc_av_SpecifiedOutputParameterAbstraction(
        ArrayList<VariableUsage> variableusages    ) {
        this.variableusages = variableusages;
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

}