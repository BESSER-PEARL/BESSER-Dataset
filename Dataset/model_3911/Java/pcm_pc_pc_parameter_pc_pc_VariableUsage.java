





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_parameter_pc_pc_VariableUsage  {






    private SynchronisationPoint synchronisationpoint;




    private CallAction callaction;




    private List<VariableCharacterisation> variablecharacterisations;




    private EntryLevelSystemCall entrylevelsystemcall;




    private parameter_pc_pc_pcm_pc_pc_AbstractNamedReference parameter_pc_pc_pcm_pc_pc_abstractnamedreference;




    private CallReturnAction callreturnaction;




    private SetVariableAction setvariableaction;




    private composition_pc_pc_AssemblyContext composition_pc_pc_assemblycontext;




    private EntryLevelSystemCall entrylevelsystemcall;




    private SpecifiedOutputParameterAbstraction specifiedoutputparameterabstraction;




    private UserData userdata;


    public pcm_pc_pc_parameter_pc_pc_VariableUsage(
    ) {
        this.variablecharacterisations = new ArrayList<>();
    }

    public pcm_pc_pc_parameter_pc_pc_VariableUsage(
        ArrayList<VariableCharacterisation> variablecharacterisations    ) {
        this.variablecharacterisations = variablecharacterisations;
    }


    public SynchronisationPoint getSynchronisationpoint() {
        return synchronisationpoint;
    }

    public void setSynchronisationpoint(SynchronisationPoint synchronisationpoint) {
        this.synchronisationpoint = synchronisationpoint;
    }
    public CallAction getCallaction() {
        return callaction;
    }

    public void setCallaction(CallAction callaction) {
        this.callaction = callaction;
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
    public parameter_pc_pc_pcm_pc_pc_AbstractNamedReference getParameter_pc_pc_pcm_pc_pc_abstractnamedreference() {
        return parameter_pc_pc_pcm_pc_pc_abstractnamedreference;
    }

    public void setParameter_pc_pc_pcm_pc_pc_abstractnamedreference(parameter_pc_pc_pcm_pc_pc_AbstractNamedReference parameter_pc_pc_pcm_pc_pc_abstractnamedreference) {
        this.parameter_pc_pc_pcm_pc_pc_abstractnamedreference = parameter_pc_pc_pcm_pc_pc_abstractnamedreference;
    }
    public CallReturnAction getCallreturnaction() {
        return callreturnaction;
    }

    public void setCallreturnaction(CallReturnAction callreturnaction) {
        this.callreturnaction = callreturnaction;
    }
    public SetVariableAction getSetvariableaction() {
        return setvariableaction;
    }

    public void setSetvariableaction(SetVariableAction setvariableaction) {
        this.setvariableaction = setvariableaction;
    }
    public composition_pc_pc_AssemblyContext getComposition_pc_pc_assemblycontext() {
        return composition_pc_pc_assemblycontext;
    }

    public void setComposition_pc_pc_assemblycontext(composition_pc_pc_AssemblyContext composition_pc_pc_assemblycontext) {
        this.composition_pc_pc_assemblycontext = composition_pc_pc_assemblycontext;
    }
    public EntryLevelSystemCall getEntrylevelsystemcall() {
        return entrylevelsystemcall;
    }

    public void setEntrylevelsystemcall(EntryLevelSystemCall entrylevelsystemcall) {
        this.entrylevelsystemcall = entrylevelsystemcall;
    }
    public SpecifiedOutputParameterAbstraction getSpecifiedoutputparameterabstraction() {
        return specifiedoutputparameterabstraction;
    }

    public void setSpecifiedoutputparameterabstraction(SpecifiedOutputParameterAbstraction specifiedoutputparameterabstraction) {
        this.specifiedoutputparameterabstraction = specifiedoutputparameterabstraction;
    }
    public UserData getUserdata() {
        return userdata;
    }

    public void setUserdata(UserData userdata) {
        this.userdata = userdata;
    }

}