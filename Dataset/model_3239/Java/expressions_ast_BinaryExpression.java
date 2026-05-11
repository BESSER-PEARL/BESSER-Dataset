





import java.util.List;
import java.util.ArrayList;

public class expressions_ast_BinaryExpression extends Expression {

    private String operation;



    public expressions_ast_BinaryExpression(
        String operation    ) {
        super(
        );
        this.operation = operation;
    }


    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }


}