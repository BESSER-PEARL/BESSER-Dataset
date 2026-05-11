





import java.util.List;
import java.util.ArrayList;

public class actionpak1_IncomingCall2 extends call_CallSource1, actionstep_ParameterizedInitiator {

    private String callName;



    public actionpak1_IncomingCall2(
        String callName    ) {
        super(
        );
        this.callName = callName;
    }


    public String getCallname() {
        return callName;
    }

    public void setCallname(String callName) {
        this.callName = callName;
    }


}