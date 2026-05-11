





import java.util.List;
import java.util.ArrayList;

public class optGrammar_FunctionCallListArguments extends FunctionCallArguments {






    private optGrammar_NewExpression optgrammar_newexpression;




    private optGrammar_ModifierInvocation optgrammar_modifierinvocation;




    private List<optGrammar_Expression> optgrammar_expressions;




    private optGrammar_InheritanceSpecifier optgrammar_inheritancespecifier;


    public optGrammar_FunctionCallListArguments(
    ) {
        super(
        );
        this.optgrammar_expressions = new ArrayList<>();
    }

    public optGrammar_FunctionCallListArguments(
        ArrayList<optGrammar_Expression> optgrammar_expressions    ) {
        this.optgrammar_expressions = optgrammar_expressions;
    }


    public optGrammar_NewExpression getOptgrammar_newexpression() {
        return optgrammar_newexpression;
    }

    public void setOptgrammar_newexpression(optGrammar_NewExpression optgrammar_newexpression) {
        this.optgrammar_newexpression = optgrammar_newexpression;
    }
    public optGrammar_ModifierInvocation getOptgrammar_modifierinvocation() {
        return optgrammar_modifierinvocation;
    }

    public void setOptgrammar_modifierinvocation(optGrammar_ModifierInvocation optgrammar_modifierinvocation) {
        this.optgrammar_modifierinvocation = optgrammar_modifierinvocation;
    }
    public List<optGrammar_Expression> getOptgrammar_expressions() {
        return optgrammar_expressions;
    }

    public void addOptgrammar_expression(Optgrammar_expression optgrammar_expression) {
        this.optgrammar_expressions.add(optgrammar_expression);
    }
    public optGrammar_InheritanceSpecifier getOptgrammar_inheritancespecifier() {
        return optgrammar_inheritancespecifier;
    }

    public void setOptgrammar_inheritancespecifier(optGrammar_InheritanceSpecifier optgrammar_inheritancespecifier) {
        this.optgrammar_inheritancespecifier = optgrammar_inheritancespecifier;
    }

}