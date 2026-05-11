





import java.util.List;
import java.util.ArrayList;

public class ftp_SignalValue extends TypedPortValue {

    private String signal;



    public ftp_SignalValue(
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