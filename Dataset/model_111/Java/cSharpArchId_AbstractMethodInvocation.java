





import java.util.List;
import java.util.ArrayList;

public class cSharpArchId_AbstractMethodInvocation extends ASTNode {






    private List<cSharpArchId_Expresion> csharparchid_expresions;


    public cSharpArchId_AbstractMethodInvocation(
    ) {
        super(
        );
        this.csharparchid_expresions = new ArrayList<>();
    }

    public cSharpArchId_AbstractMethodInvocation(
        ArrayList<cSharpArchId_Expresion> csharparchid_expresions    ) {
        this.csharparchid_expresions = csharparchid_expresions;
    }


    public List<cSharpArchId_Expresion> getCsharparchid_expresions() {
        return csharparchid_expresions;
    }

    public void addCsharparchid_expresion(Csharparchid_expresion csharparchid_expresion) {
        this.csharparchid_expresions.add(csharparchid_expresion);
    }

}