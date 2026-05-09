





import java.util.List;
import java.util.ArrayList;

public class uml_SendSignalAction extends InvocationAction {






    private uml_Signal uml_signal;




    private uml_InputPin uml_inputpin;


    public uml_SendSignalAction(
    ) {
        super(
        );
    }



    public uml_Signal getUml_signal() {
        return uml_signal;
    }

    public void setUml_signal(uml_Signal uml_signal) {
        this.uml_signal = uml_signal;
    }
    public uml_InputPin getUml_inputpin() {
        return uml_inputpin;
    }

    public void setUml_inputpin(uml_InputPin uml_inputpin) {
        this.uml_inputpin = uml_inputpin;
    }

}