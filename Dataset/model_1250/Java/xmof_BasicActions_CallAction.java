





import java.util.List;
import java.util.ArrayList;

public class xmof_BasicActions_CallAction extends InvocationAction {

    private boolean synchronous;



    public xmof_BasicActions_CallAction(
        boolean synchronous    ) {
        super(
        );
        this.synchronous = synchronous;
    }


    public boolean getSynchronous() {
        return synchronous;
    }

    public void setSynchronous(boolean synchronous) {
        this.synchronous = synchronous;
    }


}