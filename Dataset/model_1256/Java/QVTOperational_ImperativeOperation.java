





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ImperativeOperation  {

    private String isBlackbox;





    private OperationBody operationbody;




    private ImperativeOperation imperativeoperation;




    private List<VarParameter> varparameters;




    private VarParameter varparameter;


    public QVTOperational_ImperativeOperation(
        String isBlackbox    ) {
        this.isBlackbox = isBlackbox;
        this.varparameters = new ArrayList<>();
    }

    public QVTOperational_ImperativeOperation(
        String isBlackbox        ArrayList<VarParameter> varparameters    ) {
        this.isBlackbox = isBlackbox;
        this.varparameters = varparameters;
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
    public List<VarParameter> getVarparameters() {
        return varparameters;
    }

    public void addVarparameter(Varparameter varparameter) {
        this.varparameters.add(varparameter);
    }
    public VarParameter getVarparameter() {
        return varparameter;
    }

    public void setVarparameter(VarParameter varparameter) {
        this.varparameter = varparameter;
    }

}