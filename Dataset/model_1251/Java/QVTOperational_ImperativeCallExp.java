





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ImperativeCallExp extends OperationCallExp, ImperativeExpression {

    private String isVirtual;



    public QVTOperational_ImperativeCallExp(
        String isVirtual    ) {
        super(
        );
        this.isVirtual = isVirtual;
    }


    public String getIsvirtual() {
        return isVirtual;
    }

    public void setIsvirtual(String isVirtual) {
        this.isVirtual = isVirtual;
    }


}