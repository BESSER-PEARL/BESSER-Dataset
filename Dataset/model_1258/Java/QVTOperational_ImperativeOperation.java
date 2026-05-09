





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ImperativeOperation  {

    private String isBlackbox;





    private OperationBody operationbody;




    private ImperativeOperation imperativeoperation;


    public QVTOperational_ImperativeOperation(
        String isBlackbox    ) {
        this.isBlackbox = isBlackbox;
    }


    public String getIsblackbox() {
        return isBlackbox;
    }

    public void setIsblackbox(String isBlackbox) {
        this.isBlackbox = isBlackbox;
    }

    public OperationBody getOperationbody() {
        return operationbody;
    }

    public void setOperationbody(OperationBody operationbody) {
        this.operationbody = operationbody;
    }
    public ImperativeOperation getImperativeoperation() {
        return imperativeoperation;
    }

    public void setImperativeoperation(ImperativeOperation imperativeoperation) {
        this.imperativeoperation = imperativeoperation;
    }

}