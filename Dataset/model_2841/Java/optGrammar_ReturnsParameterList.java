





import java.util.List;
import java.util.ArrayList;

public class optGrammar_ReturnsParameterList  {






    private optGrammar_FunctionDefinition optgrammar_functiondefinition;




    private List<optGrammar_ReturnParameterDeclaration> optgrammar_returnparameterdeclarations;


    public optGrammar_ReturnsParameterList(
    ) {
        this.optgrammar_returnparameterdeclarations = new ArrayList<>();
    }

    public optGrammar_ReturnsParameterList(
        ArrayList<optGrammar_ReturnParameterDeclaration> optgrammar_returnparameterdeclarations    ) {
        this.optgrammar_returnparameterdeclarations = optgrammar_returnparameterdeclarations;
    }


    public optGrammar_FunctionDefinition getOptgrammar_functiondefinition() {
        return optgrammar_functiondefinition;
    }

    public void setOptgrammar_functiondefinition(optGrammar_FunctionDefinition optgrammar_functiondefinition) {
        this.optgrammar_functiondefinition = optgrammar_functiondefinition;
    }
    public List<optGrammar_ReturnParameterDeclaration> getOptgrammar_returnparameterdeclarations() {
        return optgrammar_returnparameterdeclarations;
    }

    public void addOptgrammar_returnparameterdeclaration(Optgrammar_returnparameterdeclaration optgrammar_returnparameterdeclaration) {
        this.optgrammar_returnparameterdeclarations.add(optgrammar_returnparameterdeclaration);
    }

}