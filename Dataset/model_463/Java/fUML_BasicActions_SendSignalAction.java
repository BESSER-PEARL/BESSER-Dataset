





import java.util.List;
import java.util.ArrayList;

public class fUML_BasicActions_SendSignalAction extends InvocationAction {






    private BasicActions_InputPin basicactions_inputpin;




    private Communications_Signal communications_signal;


    public fUML_BasicActions_SendSignalAction(
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
    public Communications_Signal getCommunications_signal() {
        return communications_signal;
    }

    public void setCommunications_signal(Communications_Signal communications_signal) {
        this.communications_signal = communications_signal;
    }

}