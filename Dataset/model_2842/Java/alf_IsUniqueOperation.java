





import java.util.List;
import java.util.ArrayList;

public class alf_IsUniqueOperation extends SequenceExpansionExpression {

    private String name;





    private alf_Expression alf_expression;


    public alf_IsUniqueOperation(
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

    public alf_Expression getAlf_expression() {
        return alf_expression;
    }

    public void setAlf_expression(alf_Expression alf_expression) {
        this.alf_expression = alf_expression;
    }

}