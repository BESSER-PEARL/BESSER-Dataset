





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_TemplateInstantiation  {






    private Identifier identifier;




    private List<expressions_Expression> expressions_expressions;




    private Identifier identifier;




    private List<declarations_TAParameter> declarations_taparameters;


    public timedAutomata_core_TemplateInstantiation(
    ) {
        this.expressions_expressions = new ArrayList<>();
        this.declarations_taparameters = new ArrayList<>();
    }

    public timedAutomata_core_TemplateInstantiation(
        ArrayList<expressions_Expression> expressions_expressions,        ArrayList<declarations_TAParameter> declarations_taparameters    ) {
        this.expressions_expressions = expressions_expressions;
        this.declarations_taparameters = declarations_taparameters;
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

}