





import java.util.List;
import java.util.ArrayList;

public class model_AbstractCExpression  {






    private model_AbstractMFieldDeclaration model_abstractmfielddeclaration;




    private model_CDeclarationStatement model_cdeclarationstatement;


    public model_AbstractCExpression(
    ) {
    }



    public model_AbstractMFieldDeclaration getModel_abstractmfielddeclaration() {
        return model_abstractmfielddeclaration;
    }

    public void setModel_abstractmfielddeclaration(model_AbstractMFieldDeclaration model_abstractmfielddeclaration) {
        this.model_abstractmfielddeclaration = model_abstractmfielddeclaration;
    }
    public model_CDeclarationStatement getModel_cdeclarationstatement() {
        return model_cdeclarationstatement;
    }

    public void setModel_cdeclarationstatement(model_CDeclarationStatement model_cdeclarationstatement) {
        this.model_cdeclarationstatement = model_cdeclarationstatement;
    }

}