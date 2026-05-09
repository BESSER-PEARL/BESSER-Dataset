





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionCallExpression extends Expression {






    private astm_Expression astm_expression;




    private List<astm_OtherSyntaxObject> astm_othersyntaxobjects;


    public astm_FunctionCallExpression(
    ) {
        super(
        );
        this.astm_othersyntaxobjects = new ArrayList<>();
    }

    public astm_FunctionCallExpression(
        ArrayList<astm_OtherSyntaxObject> astm_othersyntaxobjects    ) {
        this.astm_othersyntaxobjects = astm_othersyntaxobjects;
    }


    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }
    public List<astm_OtherSyntaxObject> getAstm_othersyntaxobjects() {
        return astm_othersyntaxobjects;
    }

    public void addAstm_othersyntaxobject(Astm_othersyntaxobject astm_othersyntaxobject) {
        this.astm_othersyntaxobjects.add(astm_othersyntaxobject);
    }

}