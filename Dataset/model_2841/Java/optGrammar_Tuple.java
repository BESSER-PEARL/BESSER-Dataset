





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Tuple extends Expression {






    private optGrammar_VarVariableTupleVariableDeclaration optgrammar_varvariabletuplevariabledeclaration;




    private List<optGrammar_Expression> optgrammar_expressions;


    public optGrammar_Tuple(
    ) {
        super(
        );
        this.optgrammar_expressions = new ArrayList<>();
    }

    public optGrammar_Tuple(
        ArrayList<optGrammar_Expression> optgrammar_expressions    ) {
        this.optgrammar_expressions = optgrammar_expressions;
    }


    public optGrammar_VarVariableTupleVariableDeclaration getOptgrammar_varvariabletuplevariabledeclaration() {
        return optgrammar_varvariabletuplevariabledeclaration;
    }

    public void setOptgrammar_varvariabletuplevariabledeclaration(optGrammar_VarVariableTupleVariableDeclaration optgrammar_varvariabletuplevariabledeclaration) {
        this.optgrammar_varvariabletuplevariabledeclaration = optgrammar_varvariabletuplevariabledeclaration;
    }
    public List<optGrammar_Expression> getOptgrammar_expressions() {
        return optgrammar_expressions;
    }

    public void addOptgrammar_expression(Optgrammar_expression optgrammar_expression) {
        this.optgrammar_expressions.add(optgrammar_expression);
    }

}