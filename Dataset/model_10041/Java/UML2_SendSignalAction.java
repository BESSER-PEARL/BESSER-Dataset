





import java.util.List;
import java.util.ArrayList;

public class UML2_SendSignalAction extends InvocationAction {






    private UML2_Signal uml2_signal;




    private UML2_InputPin uml2_inputpin;


    public UML2_SendSignalAction(
    ) {
        super(
        );
    }



    public UML2_Signal getUml2_signal() {
        return uml2_signal;
    }

    public void setUml2_signal(UML2_Signal uml2_signal) {
        this.uml2_signal = uml2_signal;
    }
    public UML2_InputPin getUml2_inputpin() {
        return uml2_inputpin;
    }

    public void setUml2_inputpin(UML2_InputPin uml2_inputpin) {
        this.uml2_inputpin = uml2_inputpin;
    }

}