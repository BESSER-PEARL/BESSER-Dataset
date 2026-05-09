





import java.util.List;
import java.util.ArrayList;

public class uml_ReceiveSignalEvent extends MessageEvent {






    private uml_Signal uml_signal;


    public uml_ReceiveSignalEvent(
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

}