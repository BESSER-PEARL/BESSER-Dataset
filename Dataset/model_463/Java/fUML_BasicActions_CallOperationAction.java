





import java.util.List;
import java.util.ArrayList;

public class fUML_BasicActions_CallOperationAction extends CallAction {






    private BasicActions_InputPin basicactions_inputpin;




    private Kernel_Operation kernel_operation;


    public fUML_BasicActions_CallOperationAction(
    ) {
        super(
        );
    }



    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }
    public Kernel_Operation getKernel_operation() {
        return kernel_operation;
    }

    public void setKernel_operation(Kernel_Operation kernel_operation) {
        this.kernel_operation = kernel_operation;
    }

}