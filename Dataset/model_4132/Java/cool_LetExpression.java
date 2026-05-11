





import java.util.List;
import java.util.ArrayList;

public class cool_LetExpression extends PrimaryExpression {






    private List<cool_LetDeclaration> cool_letdeclarations;




    private cool_Expression cool_expression;


    public cool_LetExpression(
    ) {
        super(
        );
        this.cool_letdeclarations = new ArrayList<>();
    }

    public cool_LetExpression(
        ArrayList<cool_LetDeclaration> cool_letdeclarations    ) {
        this.cool_letdeclarations = cool_letdeclarations;
    }


    public List<cool_LetDeclaration> getCool_letdeclarations() {
        return cool_letdeclarations;
    }

    public void addCool_letdeclaration(Cool_letdeclaration cool_letdeclaration) {
        this.cool_letdeclarations.add(cool_letdeclaration);
    }
    public cool_Expression getCool_expression() {
        return cool_expression;
    }

    public void setCool_expression(cool_Expression cool_expression) {
        this.cool_expression = cool_expression;
    }

}