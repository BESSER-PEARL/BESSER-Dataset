





import java.util.List;
import java.util.ArrayList;

public class component_CorbaExecutionContext extends ExecutionContext, CorbaWrapperObject {

    private String rtcExecutionContextProfile;



    public component_CorbaExecutionContext(
        String rtcExecutionContextProfile    ) {
        super(
        );
        this.rtcExecutionContextProfile = rtcExecutionContextProfile;
    }


    public String getRtcexecutioncontextprofile() {
        return rtcExecutionContextProfile;
    }

    public void setRtcexecutioncontextprofile(String rtcExecutionContextProfile) {
        this.rtcExecutionContextProfile = rtcExecutionContextProfile;
    }


}