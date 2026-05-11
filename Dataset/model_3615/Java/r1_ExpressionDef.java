





import java.util.List;
import java.util.ArrayList;

public class r1_ExpressionDef extends Element {

    private String name;
    private String accessLevel;
    private String context;





    private r1_Expression r1_expression;


    public r1_ExpressionDef(
        String name,        String accessLevel,        String context    ) {
        super(
        );
        this.name = name;
        this.accessLevel = accessLevel;
        this.context = context;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }
    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public r1_Expression getR1_expression() {
        return r1_expression;
    }

    public void setR1_expression(r1_Expression r1_expression) {
        this.r1_expression = r1_expression;
    }

}