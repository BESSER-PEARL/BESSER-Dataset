





import java.util.List;
import java.util.ArrayList;

public class aspectualacme_ArmaniFunctionCall extends ArmaniPrimitiveExpression {

    private String functionId;



    public aspectualacme_ArmaniFunctionCall(
        String functionId    ) {
        super(
        );
        this.functionId = functionId;
    }


    public String getFunctionid() {
        return functionId;
    }

    public void setFunctionid(String functionId) {
        this.functionId = functionId;
    }


}