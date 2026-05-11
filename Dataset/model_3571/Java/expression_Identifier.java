





import java.util.List;
import java.util.ArrayList;

public class expression_Identifier extends SyntaxElement {

    private String id;
    private String cl;





    private expression_Identifier expression_identifier;


    public expression_Identifier(
        String id,        String cl    ) {
        super(
        );
        this.id = id;
        this.cl = cl;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getCl() {
        return cl;
    }

    public void setCl(String cl) {
        this.cl = cl;
    }

    public expression_Identifier getExpression_identifier() {
        return expression_identifier;
    }

    public void setExpression_identifier(expression_Identifier expression_identifier) {
        this.expression_identifier = expression_identifier;
    }

}