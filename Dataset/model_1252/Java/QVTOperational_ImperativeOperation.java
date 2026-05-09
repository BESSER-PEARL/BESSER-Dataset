





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ImperativeOperation extends Operation {

    private String isBlackbox;





    private ImperativeOperation imperativeoperation;




    private OperationBody operationbody;


    public QVTOperational_ImperativeOperation(
        String isBlackbox    ) {
        super(
        );
        this.isBlackbox = isBlackbox;
    }


    public String getIsblackbox() {
        return isBlackbox;
    }

    public void setIsblackbox(String isBlackbox) {
        this.isBlackbox = isBlackbox;
    }

    public ImperativeOperation getImperativeoperation() {
        return imperativeoperation;
    }

    public void setImperativeoperation(ImperativeOperation imperativeoperation) {
        this.imperativeoperation = imperativeoperation;
    }
    public OperationBody getOperationbody() {
        return operationbody;
    }

    public void setOperationbody(OperationBody operationbody) {
        this.operationbody = operationbody;
    }

}