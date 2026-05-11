





import java.util.List;
import java.util.ArrayList;

public class optGrammar_ParameterList  {






    private optGrammar_FunctionDefinition optgrammar_functiondefinition;




    private optGrammar_Event optgrammar_event;




    private List<optGrammar_PrimaryTypeDefinitionDeclaration> optgrammar_primarytypedefinitiondeclarations;




    private optGrammar_ConstructorDefinition optgrammar_constructordefinition;




    private optGrammar_Modifier optgrammar_modifier;


    public optGrammar_ParameterList(
    ) {
        this.optgrammar_primarytypedefinitiondeclarations = new ArrayList<>();
    }

    public optGrammar_ParameterList(
        ArrayList<optGrammar_PrimaryTypeDefinitionDeclaration> optgrammar_primarytypedefinitiondeclarations    ) {
        this.optgrammar_primarytypedefinitiondeclarations = optgrammar_primarytypedefinitiondeclarations;
    }


    public optGrammar_FunctionDefinition getOptgrammar_functiondefinition() {
        return optgrammar_functiondefinition;
    }

    public void setOptgrammar_functiondefinition(optGrammar_FunctionDefinition optgrammar_functiondefinition) {
        this.optgrammar_functiondefinition = optgrammar_functiondefinition;
    }
    public optGrammar_Event getOptgrammar_event() {
        return optgrammar_event;
    }

    public void setOptgrammar_event(optGrammar_Event optgrammar_event) {
        this.optgrammar_event = optgrammar_event;
    }
    public List<optGrammar_PrimaryTypeDefinitionDeclaration> getOptgrammar_primarytypedefinitiondeclarations() {
        return optgrammar_primarytypedefinitiondeclarations;
    }

    public void addOptgrammar_primarytypedefinitiondeclaration(Optgrammar_primarytypedefinitiondeclaration optgrammar_primarytypedefinitiondeclaration) {
        this.optgrammar_primarytypedefinitiondeclarations.add(optgrammar_primarytypedefinitiondeclaration);
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

}