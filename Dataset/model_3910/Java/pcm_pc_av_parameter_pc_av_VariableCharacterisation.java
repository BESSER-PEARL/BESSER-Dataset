





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_parameter_pc_av_VariableCharacterisation  {

    private String type;





    private VariableUsage variableusage;




    private PCMRandomVariable pcmrandomvariable;


    public pcm_pc_av_parameter_pc_av_VariableCharacterisation(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public VariableUsage getVariableusage() {
        return variableusage;
    }

    public void setVariableusage(VariableUsage variableusage) {
        this.variableusage = variableusage;
    }
    public PCMRandomVariable getPcmrandomvariable() {
        return pcmrandomvariable;
    }

    public void setPcmrandomvariable(PCMRandomVariable pcmrandomvariable) {
        this.pcmrandomvariable = pcmrandomvariable;
    }

}