





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Body extends Statement {






    private optGrammar_ConstructorDefinition optgrammar_constructordefinition;




    private optGrammar_Modifier optgrammar_modifier;




    private List<optGrammar_Statement> optgrammar_statements;




    private optGrammar_FunctionDefinition optgrammar_functiondefinition;


    public optGrammar_Body(
    ) {
        super(
        );
        this.optgrammar_statements = new ArrayList<>();
    }

    public optGrammar_Body(
        ArrayList<optGrammar_Statement> optgrammar_statements    ) {
        this.optgrammar_statements = optgrammar_statements;
    }


    public optGrammar_ConstructorDefinition getOptgrammar_constructordefinition() {
        return optgrammar_constructordefinition;
    }

    public void setOptgrammar_constructordefinition(optGrammar_ConstructorDefinition optgrammar_constructordefinition) {
        this.optgrammar_constructordefinition = optgrammar_constructordefinition;
    }
    public optGrammar_Modifier getOptgrammar_modifier() {
        return optgrammar_modifier;
    }

    public void setOptgrammar_modifier(optGrammar_Modifier optgrammar_modifier) {
        this.optgrammar_modifier = optgrammar_modifier;
    }
    public List<optGrammar_Statement> getOptgrammar_statements() {
        return optgrammar_statements;
    }

    public void addOptgrammar_statement(Optgrammar_statement optgrammar_statement) {
        this.optgrammar_statements.add(optgrammar_statement);
    }
    public optGrammar_FunctionDefinition getOptgrammar_functiondefinition() {
        return optgrammar_functiondefinition;
    }

    public void setOptgrammar_functiondefinition(optGrammar_FunctionDefinition optgrammar_functiondefinition) {
        this.optgrammar_functiondefinition = optgrammar_functiondefinition;
    }

}