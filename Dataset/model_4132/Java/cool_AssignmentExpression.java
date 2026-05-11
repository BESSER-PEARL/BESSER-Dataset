





import java.util.List;
import java.util.ArrayList;

public class cool_AssignmentExpression extends PrimaryExpression {

    private String name;





    private cool_Expression cool_expression;


    public cool_AssignmentExpression(
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

    public cool_Expression getCool_expression() {
        return cool_expression;
    }

    public void setCool_expression(cool_Expression cool_expression) {
        this.cool_expression = cool_expression;
    }

}