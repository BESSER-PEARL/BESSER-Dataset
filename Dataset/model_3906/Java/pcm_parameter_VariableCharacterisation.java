





import java.util.List;
import java.util.ArrayList;

public class pcm_parameter_VariableCharacterisation  {

    private String type;





    private PCMRandomVariable pcmrandomvariable;


    public pcm_parameter_VariableCharacterisation(
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

}