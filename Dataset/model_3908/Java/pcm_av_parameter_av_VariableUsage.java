





import java.util.List;
import java.util.ArrayList;

public class pcm_av_parameter_av_VariableUsage  {






    private composition_av_AssemblyContext composition_av_assemblycontext;




    private List<VariableCharacterisation> variablecharacterisations;




    private UserData userdata;




    private EntryLevelSystemCall entrylevelsystemcall;




    private EntryLevelSystemCall entrylevelsystemcall;


    public pcm_av_parameter_av_VariableUsage(
    ) {
        this.variablecharacterisations = new ArrayList<>();
    }

    public pcm_av_parameter_av_VariableUsage(
        ArrayList<VariableCharacterisation> variablecharacterisations    ) {
        this.variablecharacterisations = variablecharacterisations;
    }


    public composition_av_AssemblyContext getComposition_av_assemblycontext() {
        return composition_av_assemblycontext;
    }

    public void setComposition_av_assemblycontext(composition_av_AssemblyContext composition_av_assemblycontext) {
        this.composition_av_assemblycontext = composition_av_assemblycontext;
    }
    public List<VariableCharacterisation> getVariablecharacterisations() {
        return variablecharacterisations;
    }

    public void addVariablecharacterisation(Variablecharacterisation variablecharacterisation) {
        this.variablecharacterisations.add(variablecharacterisation);
    }
    public UserData getUserdata() {
        return userdata;
    }

    public void setUserdata(UserData userdata) {
        this.userdata = userdata;
    }
    public EntryLevelSystemCall getEntrylevelsystemcall() {
        return entrylevelsystemcall;
    }

    public void setEntrylevelsystemcall(EntryLevelSystemCall entrylevelsystemcall) {
        this.entrylevelsystemcall = entrylevelsystemcall;
    }
    public EntryLevelSystemCall getEntrylevelsystemcall() {
        return entrylevelsystemcall;
    }

    public void setEntrylevelsystemcall(EntryLevelSystemCall entrylevelsystemcall) {
        this.entrylevelsystemcall = entrylevelsystemcall;
    }

}