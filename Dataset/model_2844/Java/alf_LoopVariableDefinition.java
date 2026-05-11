





import java.util.List;
import java.util.ArrayList;

public class alf_LoopVariableDefinition  {

    private String name;





    private alf_ForControl alf_forcontrol;


    public alf_LoopVariableDefinition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public alf_ForControl getAlf_forcontrol() {
        return alf_forcontrol;
    }

    public void setAlf_forcontrol(alf_ForControl alf_forcontrol) {
        this.alf_forcontrol = alf_forcontrol;
    }

}