





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_OclExpression extends LocatedElement {






    private LoopExp loopexp;




    private OperationCall operationcall;




    private LocalVariable localvariable;




    private Operation operation;


    public gbind_simpleocl_OclExpression(
    ) {
        super(
        );
    }



    public LoopExp getLoopexp() {
        return loopexp;
    }

    public void setLoopexp(LoopExp loopexp) {
        this.loopexp = loopexp;
    }
    public OperationCall getOperationcall() {
        return operationcall;
    }

    public void setOperationcall(OperationCall operationcall) {
        this.operationcall = operationcall;
    }
    public LocalVariable getLocalvariable() {
        return localvariable;
    }

    public void setLocalvariable(LocalVariable localvariable) {
        this.localvariable = localvariable;
    }
    public Operation getOperation() {
        return operation;
    }

    public void setOperation(Operation operation) {
        this.operation = operation;
    }

}