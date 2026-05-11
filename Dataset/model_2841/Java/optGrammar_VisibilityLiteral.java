





import java.util.List;
import java.util.ArrayList;

public class optGrammar_VisibilityLiteral  {

    private String type;





    private optGrammar_FunctionDefinition optgrammar_functiondefinition;




    private optGrammar_ConstructorDefinition optgrammar_constructordefinition;


    public optGrammar_VisibilityLiteral(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public optGrammar_FunctionDefinition getOptgrammar_functiondefinition() {
        return optgrammar_functiondefinition;
    }

    public void setOptgrammar_functiondefinition(optGrammar_FunctionDefinition optgrammar_functiondefinition) {
        this.optgrammar_functiondefinition = optgrammar_functiondefinition;
    }
    public optGrammar_ConstructorDefinition getOptgrammar_constructordefinition() {
        return optgrammar_constructordefinition;
    }

    public void setOptgrammar_constructordefinition(optGrammar_ConstructorDefinition optgrammar_constructordefinition) {
        this.optgrammar_constructordefinition = optgrammar_constructordefinition;
    }

}