





import java.util.List;
import java.util.ArrayList;

public class Request  {

    private None leaveApplication;
    private String requestId;



    public Request(
        None leaveApplication,        String requestId    ) {
        this.leaveApplication = leaveApplication;
        this.requestId = requestId;
    }


    public None getLeaveapplication() {
        return leaveApplication;
    }

    public void setLeaveapplication(None leaveApplication) {
        this.leaveApplication = leaveApplication;
    }
    public String getRequestid() {
        return requestId;
    }

    public void setRequestid(String requestId) {
        this.requestId = requestId;
    }


}