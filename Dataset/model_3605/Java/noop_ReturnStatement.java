





import java.util.List;
import java.util.ArrayList;

public class noop_ReturnStatement extends Statement {

    private String name;





    private noop_Expression noop_expression;


    public noop_ReturnStatement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public noop_Expression getNoop_expression() {
        return noop_expression;
    }

    public void setNoop_expression(noop_Expression noop_expression) {
        this.noop_expression = noop_expression;
    }

}