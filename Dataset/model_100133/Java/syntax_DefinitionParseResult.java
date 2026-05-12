





import java.util.List;
import java.util.ArrayList;

public class syntax_DefinitionParseResult  {






    private List<syntax_DefinitionParseError> syntax_definitionparseerrors;


    public syntax_DefinitionParseResult(
    ) {
        this.syntax_definitionparseerrors = new ArrayList<>();
    }

    public syntax_DefinitionParseResult(
        ArrayList<syntax_DefinitionParseError> syntax_definitionparseerrors    ) {
        this.syntax_definitionparseerrors = syntax_definitionparseerrors;
    }


    public List<syntax_DefinitionParseError> getSyntax_definitionparseerrors() {
        return syntax_definitionparseerrors;
    }

    public void addSyntax_definitionparseerror(Syntax_definitionparseerror syntax_definitionparseerror) {
        this.syntax_definitionparseerrors.add(syntax_definitionparseerror);
    }

}