





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Managed extends IVREvent {

    private int code;
    private boolean success;



    public stateMachine_Managed(
        int code,        boolean success    ) {
        super(
        );
        this.code = code;
        this.success = success;
    }


    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
    public boolean getSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }


}