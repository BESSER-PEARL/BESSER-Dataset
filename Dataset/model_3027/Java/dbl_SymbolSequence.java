





import java.util.List;
import java.util.ArrayList;

public class dbl_SymbolSequence extends L2SyntaxExpression {






    private List<dbl_SyntaxExpression> dbl_syntaxexpressions;


    public dbl_SymbolSequence(
    ) {
        super(
        );
        this.dbl_syntaxexpressions = new ArrayList<>();
    }

    public dbl_SymbolSequence(
        ArrayList<dbl_SyntaxExpression> dbl_syntaxexpressions    ) {
        this.dbl_syntaxexpressions = dbl_syntaxexpressions;
    }


    public List<dbl_SyntaxExpression> getDbl_syntaxexpressions() {
        return dbl_syntaxexpressions;
    }

    public void addDbl_syntaxexpression(Dbl_syntaxexpression dbl_syntaxexpression) {
        this.dbl_syntaxexpressions.add(dbl_syntaxexpression);
    }

}