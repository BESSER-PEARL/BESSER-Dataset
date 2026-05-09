





import java.util.List;
import java.util.ArrayList;

public class UMLModel_SendSignalEvent extends MessageEvent {

    private String signal;



    public UMLModel_SendSignalEvent(
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