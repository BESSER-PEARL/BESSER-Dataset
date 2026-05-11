





import java.util.List;
import java.util.ArrayList;

public class pcm_av_parameter_av_VariableCharacterisation  {

    private String type;





    private PCMRandomVariable pcmrandomvariable;




    private VariableUsage variableusage;


    public pcm_av_parameter_av_VariableCharacterisation(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public PCMRandomVariable getPcmrandomvariable() {
        return pcmrandomvariable;
    }

    public void setPcmrandomvariable(PCMRandomVariable pcmrandomvariable) {
        this.pcmrandomvariable = pcmrandomvariable;
    }
    public VariableUsage getVariableusage() {
        return variableusage;
    }

    public void setVariableusage(VariableUsage variableusage) {
        this.variableusage = variableusage;
    }

}