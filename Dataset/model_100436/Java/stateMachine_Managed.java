





import java.util.List;
import java.util.ArrayList;

public class stateMachine_Managed extends IVREvent {

    private boolean success;
    private int code;



    public stateMachine_Managed(
        boolean success,        int code    ) {
        super(
        );
        this.success = success;
        this.code = code;
    }


    public boolean getSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }
    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }


}