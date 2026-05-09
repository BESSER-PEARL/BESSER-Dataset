





import java.util.List;
import java.util.ArrayList;

public class fUML_CompleteActions_ReadIsClassifiedObjectAction extends Action {

    private boolean direct;





    private BasicActions_OutputPin basicactions_outputpin;




    private BasicActions_InputPin basicactions_inputpin;


    public fUML_CompleteActions_ReadIsClassifiedObjectAction(
        boolean direct    ) {
        super(
        );
        this.direct = direct;
    }


    public boolean getDirect() {
        return direct;
    }

    public void setDirect(boolean direct) {
        this.direct = direct;
    }

    public BasicActions_OutputPin getBasicactions_outputpin() {
        return basicactions_outputpin;
    }

    public void setBasicactions_outputpin(BasicActions_OutputPin basicactions_outputpin) {
        this.basicactions_outputpin = basicactions_outputpin;
    }
    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }

}