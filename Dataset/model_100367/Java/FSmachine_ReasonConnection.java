





import java.util.List;
import java.util.ArrayList;

public class FSmachine_ReasonConnection extends AbstractConection {

    private String reason;



    public FSmachine_ReasonConnection(
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