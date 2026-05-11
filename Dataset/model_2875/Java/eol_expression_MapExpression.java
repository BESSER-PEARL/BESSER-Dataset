





import java.util.List;
import java.util.ArrayList;

public class eol_expression_MapExpression extends Expression {






    private List<eol_expression_KeyValueExpression> eol_expression_keyvalueexpressions;


    public eol_expression_MapExpression(
    ) {
        super(
        );
        this.eol_expression_keyvalueexpressions = new ArrayList<>();
    }

    public eol_expression_MapExpression(
        ArrayList<eol_expression_KeyValueExpression> eol_expression_keyvalueexpressions    ) {
        this.eol_expression_keyvalueexpressions = eol_expression_keyvalueexpressions;
    }


    public List<eol_expression_KeyValueExpression> getEol_expression_keyvalueexpressions() {
        return eol_expression_keyvalueexpressions;
    }

    public void addEol_expression_keyvalueexpression(Eol_expression_keyvalueexpression eol_expression_keyvalueexpression) {
        this.eol_expression_keyvalueexpressions.add(eol_expression_keyvalueexpression);
    }

}