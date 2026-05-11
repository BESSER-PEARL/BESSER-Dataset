





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_parameter_pc_av_VariableUsage  {






    private EntryLevelSystemCall entrylevelsystemcall;




    private parameter_pc_av_pcm_pc_av_AbstractNamedReference parameter_pc_av_pcm_pc_av_abstractnamedreference;




    private composition_pc_av_AssemblyContext composition_pc_av_assemblycontext;




    private List<VariableCharacterisation> variablecharacterisations;




    private EntryLevelSystemCall entrylevelsystemcall;




    private UserData userdata;


    public pcm_pc_av_parameter_pc_av_VariableUsage(
    ) {
        this.variablecharacterisations = new ArrayList<>();
    }

    public pcm_pc_av_parameter_pc_av_VariableUsage(
        ArrayList<VariableCharacterisation> variablecharacterisations    ) {
        this.variablecharacterisations = variablecharacterisations;
    }


    public EntryLevelSystemCall getEntrylevelsystemcall() {
        return entrylevelsystemcall;
    }

    public void setEntrylevelsystemcall(EntryLevelSystemCall entrylevelsystemcall) {
        this.entrylevelsystemcall = entrylevelsystemcall;
    }
    public parameter_pc_av_pcm_pc_av_AbstractNamedReference getParameter_pc_av_pcm_pc_av_abstractnamedreference() {
        return parameter_pc_av_pcm_pc_av_abstractnamedreference;
    }

    public void setParameter_pc_av_pcm_pc_av_abstractnamedreference(parameter_pc_av_pcm_pc_av_AbstractNamedReference parameter_pc_av_pcm_pc_av_abstractnamedreference) {
        this.parameter_pc_av_pcm_pc_av_abstractnamedreference = parameter_pc_av_pcm_pc_av_abstractnamedreference;
    }
    public composition_pc_av_AssemblyContext getComposition_pc_av_assemblycontext() {
        return composition_pc_av_assemblycontext;
    }

    public void setComposition_pc_av_assemblycontext(composition_pc_av_AssemblyContext composition_pc_av_assemblycontext) {
        this.composition_pc_av_assemblycontext = composition_pc_av_assemblycontext;
    }
    public List<VariableCharacterisation> getVariablecharacterisations() {
        return variablecharacterisations;
    }

    public void addVariablecharacterisation(Variablecharacterisation variablecharacterisation) {
        this.variablecharacterisations.add(variablecharacterisation);
    }
    public EntryLevelSystemCall getEntrylevelsystemcall() {
        return entrylevelsystemcall;
    }

    public void setEntrylevelsystemcall(EntryLevelSystemCall entrylevelsystemcall) {
        this.entrylevelsystemcall = entrylevelsystemcall;
    }
    public UserData getUserdata() {
        return userdata;
    }

    public void setUserdata(UserData userdata) {
        this.userdata = userdata;
    }

}