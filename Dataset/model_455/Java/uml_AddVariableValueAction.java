





import java.util.List;
import java.util.ArrayList;

public class uml_AddVariableValueAction extends WriteVariableAction {

    private String isReplaceAll;





    private uml_InputPin uml_inputpin;


    public uml_AddVariableValueAction(
        String isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
    }


    public String getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(String isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public uml_InputPin getUml_inputpin() {
        return uml_inputpin;
    }

    public void setUml_inputpin(uml_InputPin uml_inputpin) {
        this.uml_inputpin = uml_inputpin;
    }

}