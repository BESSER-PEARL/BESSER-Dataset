





import java.util.List;
import java.util.ArrayList;

public class UMLModel_BroadcastSignalAction extends InvocationAction {

    private String signal;



    public UMLModel_BroadcastSignalAction(
        String signal    ) {
        super(
        );
        this.signal = signal;
    }


    public String getSignal() {
        return signal;
    }

    public void setSignal(String signal) {
        this.signal = signal;
    }


}