





import java.util.List;
import java.util.ArrayList;

public class Request  {

    private String requestId;
    private None leaveApplication;



    public Request(
        String requestId,        None leaveApplication    ) {
        this.requestId = requestId;
        this.leaveApplication = leaveApplication;
    }


    public String getRequestid() {
        return requestId;
    }

    public void setRequestid(String requestId) {
        this.requestId = requestId;
    }
    public None getLeaveapplication() {
        return leaveApplication;
    }

    public void setLeaveapplication(None leaveApplication) {
        this.leaveApplication = leaveApplication;
    }


}