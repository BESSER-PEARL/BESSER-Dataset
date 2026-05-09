





import java.util.List;
import java.util.ArrayList;

public class foundation_core_Parameter extends ModelElement {

    private String kind;





    private Expression expression;


    public foundation_core_Parameter(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}