





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_SrcReject extends SrcSignallingAction {

    private String reason;
    private String status;



    public jointPackage_CPL2SPL_SrcReject(
        String reason,        String status    ) {
        super(
        );
        this.reason = reason;
        this.status = status;
    }


    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}