





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_TemplateInstantiation  {






    private Identifier identifier;




    private List<declarations_TAParameter> declarations_taparameters;




    private Identifier identifier;




    private List<expressions_Expression> expressions_expressions;


    public timedAutomata_core_TemplateInstantiation(
    ) {
        this.declarations_taparameters = new ArrayList<>();
        this.expressions_expressions = new ArrayList<>();
    }

    public timedAutomata_core_TemplateInstantiation(
        ArrayList<declarations_TAParameter> declarations_taparameters,        ArrayList<expressions_Expression> expressions_expressions    ) {
        this.declarations_taparameters = declarations_taparameters;
        this.expressions_expressions = expressions_expressions;
    }


    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public List<declarations_TAParameter> getDeclarations_taparameters() {
        return declarations_taparameters;
    }

    public void addDeclarations_taparameter(Declarations_taparameter declarations_taparameter) {
        this.declarations_taparameters.add(declarations_taparameter);
    }
    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public List<expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }

}