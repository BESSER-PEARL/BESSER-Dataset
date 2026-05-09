





import java.util.List;
import java.util.ArrayList;

public class UML2_CallOperationAction extends CallAction {






    private UML2_InputPin uml2_inputpin;




    private UML2_Operation uml2_operation;


    public UML2_CallOperationAction(
    ) {
        super(
        );
    }



    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }
    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }

}