





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_ImperativeCallExp extends OperationCallExp, ImperativeExpression {

    private String isVirtual;



    public FlatQVT_ImperativeCallExp(
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