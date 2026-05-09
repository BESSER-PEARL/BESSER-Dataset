





import java.util.List;
import java.util.ArrayList;

public class fuml_CompleteActions_ReclassifyObjectAction extends Action {

    private boolean replaceAll;





    private BasicActions_InputPin basicactions_inputpin;


    public fuml_CompleteActions_ReclassifyObjectAction(
        boolean replaceAll    ) {
        super(
        );
        this.replaceAll = replaceAll;
    }


    public boolean getReplaceall() {
        return replaceAll;
    }

    public void setReplaceall(boolean replaceAll) {
        this.replaceAll = replaceAll;
    }

    public BasicActions_InputPin getBasicactions_inputpin() {
        return basicactions_inputpin;
    }

    public void setBasicactions_inputpin(BasicActions_InputPin basicactions_inputpin) {
        this.basicactions_inputpin = basicactions_inputpin;
    }

}