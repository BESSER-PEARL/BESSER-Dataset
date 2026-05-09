





import java.util.List;
import java.util.ArrayList;

public class uml_CallOperationAction extends CallAction {






    private uml_Operation uml_operation;




    private uml_InputPin uml_inputpin;


    public uml_CallOperationAction(
    ) {
        super(
        );
    }



    public uml_Operation getUml_operation() {
        return uml_operation;
    }

    public void setUml_operation(uml_Operation uml_operation) {
        this.uml_operation = uml_operation;
    }
    public uml_InputPin getUml_inputpin() {
        return uml_inputpin;
    }

    public void setUml_inputpin(uml_InputPin uml_inputpin) {
        this.uml_inputpin = uml_inputpin;
    }

}