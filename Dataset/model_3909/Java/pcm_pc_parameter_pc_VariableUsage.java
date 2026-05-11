





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_parameter_pc_VariableUsage  {






    private composition_pc_AssemblyContext composition_pc_assemblycontext;




    private UserData userdata;




    private List<VariableCharacterisation> variablecharacterisations;


    public pcm_pc_parameter_pc_VariableUsage(
    ) {
        this.variablecharacterisations = new ArrayList<>();
    }

    public pcm_pc_parameter_pc_VariableUsage(
        ArrayList<VariableCharacterisation> variablecharacterisations    ) {
        this.variablecharacterisations = variablecharacterisations;
    }


    public composition_pc_AssemblyContext getComposition_pc_assemblycontext() {
        return composition_pc_assemblycontext;
    }

    public void setComposition_pc_assemblycontext(composition_pc_AssemblyContext composition_pc_assemblycontext) {
        this.composition_pc_assemblycontext = composition_pc_assemblycontext;
    }
    public UserData getUserdata() {
        return userdata;
    }

    public void setUserdata(UserData userdata) {
        this.userdata = userdata;
    }
    public List<VariableCharacterisation> getVariablecharacterisations() {
        return variablecharacterisations;
    }

    public void addVariablecharacterisation(Variablecharacterisation variablecharacterisation) {
        this.variablecharacterisations.add(variablecharacterisation);
    }

}