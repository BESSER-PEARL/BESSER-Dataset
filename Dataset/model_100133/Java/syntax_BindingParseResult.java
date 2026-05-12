





import java.util.List;
import java.util.ArrayList;

public class syntax_BindingParseResult  {






    private List<syntax_BindingParseError> syntax_bindingparseerrors;


    public syntax_BindingParseResult(
    ) {
        this.syntax_bindingparseerrors = new ArrayList<>();
    }

    public syntax_BindingParseResult(
        ArrayList<syntax_BindingParseError> syntax_bindingparseerrors    ) {
        this.syntax_bindingparseerrors = syntax_bindingparseerrors;
    }


    public List<syntax_BindingParseError> getSyntax_bindingparseerrors() {
        return syntax_bindingparseerrors;
    }

    public void addSyntax_bindingparseerror(Syntax_bindingparseerror syntax_bindingparseerror) {
        this.syntax_bindingparseerrors.add(syntax_bindingparseerror);
    }

}