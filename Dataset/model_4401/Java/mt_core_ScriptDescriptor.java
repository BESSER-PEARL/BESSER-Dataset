





import java.util.List;
import java.util.ArrayList;

public class mt_core_ScriptDescriptor extends ASTNode {

    private String description;
    private String type;
    private String name;





    private Expression expression;


    public mt_core_ScriptDescriptor(
        String description,        String type,        String name    ) {
        super(
        );
        this.description = description;
        this.type = type;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}