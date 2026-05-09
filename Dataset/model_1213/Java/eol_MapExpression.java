





import java.util.List;
import java.util.ArrayList;

public class eol_MapExpression extends Expression {






    private List<eol_KeyValueExpression> eol_keyvalueexpressions;


    public eol_MapExpression(
    ) {
        super(
        );
        this.eol_keyvalueexpressions = new ArrayList<>();
    }

    public eol_MapExpression(
        ArrayList<eol_KeyValueExpression> eol_keyvalueexpressions    ) {
        this.eol_keyvalueexpressions = eol_keyvalueexpressions;
    }


    public List<eol_KeyValueExpression> getEol_keyvalueexpressions() {
        return eol_keyvalueexpressions;
    }

    public void addEol_keyvalueexpression(Eol_keyvalueexpression eol_keyvalueexpression) {
        this.eol_keyvalueexpressions.add(eol_keyvalueexpression);
    }

}