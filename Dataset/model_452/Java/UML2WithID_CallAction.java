





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_CallAction extends InvocationAction {

    private boolean isSynchronous;



    public UML2WithID_CallAction(
        boolean isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
    }


    public boolean getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(boolean isSynchronous) {
        this.isSynchronous = isSynchronous;
    }


}