





import java.util.List;
import java.util.ArrayList;

public class pcm_av_av_parameter_av_av_VariableUsage  {






    private List<VariableCharacterisation> variablecharacterisations;




    private composition_av_av_AssemblyContext composition_av_av_assemblycontext;


    public pcm_av_av_parameter_av_av_VariableUsage(
    ) {
        this.variablecharacterisations = new ArrayList<>();
    }

    public pcm_av_av_parameter_av_av_VariableUsage(
        ArrayList<VariableCharacterisation> variablecharacterisations    ) {
        this.variablecharacterisations = variablecharacterisations;
    }


    public List<VariableCharacterisation> getVariablecharacterisations() {
        return variablecharacterisations;
    }

    public void addVariablecharacterisation(Variablecharacterisation variablecharacterisation) {
        this.variablecharacterisations.add(variablecharacterisation);
    }
    public composition_av_av_AssemblyContext getComposition_av_av_assemblycontext() {
        return composition_av_av_assemblycontext;
    }

    public void setComposition_av_av_assemblycontext(composition_av_av_AssemblyContext composition_av_av_assemblycontext) {
        this.composition_av_av_assemblycontext = composition_av_av_assemblycontext;
    }

}