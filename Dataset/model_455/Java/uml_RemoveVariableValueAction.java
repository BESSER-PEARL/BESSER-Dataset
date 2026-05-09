





import java.util.List;
import java.util.ArrayList;

public class uml_RemoveVariableValueAction extends WriteVariableAction {

    private String isRemoveDuplicates;





    private uml_InputPin uml_inputpin;


    public uml_RemoveVariableValueAction(
        String isRemoveDuplicates    ) {
        super(
        );
        this.isRemoveDuplicates = isRemoveDuplicates;
    }


    public String getIsremoveduplicates() {
        return isRemoveDuplicates;
    }

    public void setIsremoveduplicates(String isRemoveDuplicates) {
        this.isRemoveDuplicates = isRemoveDuplicates;
    }

    public uml_InputPin getUml_inputpin() {
        return uml_inputpin;
    }

    public void setUml_inputpin(uml_InputPin uml_inputpin) {
        this.uml_inputpin = uml_inputpin;
    }

}