





import java.util.List;
import java.util.ArrayList;

public class astm_UnaryExpression extends Expression {






    private astm_OtherSyntaxObject astm_othersyntaxobject;




    private astm_Expression astm_expression;


    public astm_UnaryExpression(
    ) {
        super(
        );
    }



    public astm_OtherSyntaxObject getAstm_othersyntaxobject() {
        return astm_othersyntaxobject;
    }

    public void setAstm_othersyntaxobject(astm_OtherSyntaxObject astm_othersyntaxobject) {
        this.astm_othersyntaxobject = astm_othersyntaxobject;
    }
    public astm_Expression getAstm_expression() {
        return astm_expression;
    }

    public void setAstm_expression(astm_Expression astm_expression) {
        this.astm_expression = astm_expression;
    }

}