





import java.util.List;
import java.util.ArrayList;

public class CommonBehavior_Communications_SignalEvent extends MessageEvent {






    private Signal signal;


    public CommonBehavior_Communications_SignalEvent(
    ) {
        super(
        );
    }



    public Signal getSignal() {
        return signal;
    }

    public void setSignal(Signal signal) {
        this.signal = signal;
    }

}