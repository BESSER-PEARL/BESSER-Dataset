





import java.util.List;
import java.util.ArrayList;

public class trace_Failure extends Step {

    private String reason;



    public trace_Failure(
        String reason    ) {
        super(
        );
        this.reason = reason;
    }


    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }


}