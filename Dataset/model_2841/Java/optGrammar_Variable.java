





import java.util.List;
import java.util.ArrayList;

public class optGrammar_Variable  {

    private String name;





    private optGrammar_ReturnParameterDeclaration optgrammar_returnparameterdeclaration;




    private optGrammar_VarVariableTypeDeclaration optgrammar_varvariabletypedeclaration;




    private optGrammar_StandardVariableDeclaration optgrammar_standardvariabledeclaration;


    public optGrammar_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public optGrammar_ReturnParameterDeclaration getOptgrammar_returnparameterdeclaration() {
        return optgrammar_returnparameterdeclaration;
    }

    public void setOptgrammar_returnparameterdeclaration(optGrammar_ReturnParameterDeclaration optgrammar_returnparameterdeclaration) {
        this.optgrammar_returnparameterdeclaration = optgrammar_returnparameterdeclaration;
    }
    public optGrammar_VarVariableTypeDeclaration getOptgrammar_varvariabletypedeclaration() {
        return optgrammar_varvariabletypedeclaration;
    }

    public void setOptgrammar_varvariabletypedeclaration(optGrammar_VarVariableTypeDeclaration optgrammar_varvariabletypedeclaration) {
        this.optgrammar_varvariabletypedeclaration = optgrammar_varvariabletypedeclaration;
    }
    public optGrammar_StandardVariableDeclaration getOptgrammar_standardvariabledeclaration() {
        return optgrammar_standardvariabledeclaration;
    }

    public void setOptgrammar_standardvariabledeclaration(optGrammar_StandardVariableDeclaration optgrammar_standardvariabledeclaration) {
        this.optgrammar_standardvariabledeclaration = optgrammar_standardvariabledeclaration;
    }

}