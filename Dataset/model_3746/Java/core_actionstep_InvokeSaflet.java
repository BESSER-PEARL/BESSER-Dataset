





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_InvokeSaflet extends ActionStep {

    private String labelText;



    public core_actionstep_InvokeSaflet(
        String labelText    ) {
        super(
        );
        this.labelText = labelText;
    }


    public String getLabeltext() {
        return labelText;
    }

    public void setLabeltext(String labelText) {
        this.labelText = labelText;
    }


}