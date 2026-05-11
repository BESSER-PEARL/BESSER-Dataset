





import java.util.List;
import java.util.ArrayList;

public class alf_NameExpression extends NonLiteralValueSpecification, ValueSpecification {

    private String id;
    private String postfixOp;
    private String prefixOp;





    private alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement;


    public alf_NameExpression(
        String id,        String postfixOp,        String prefixOp    ) {
        super(
        );
        this.id = id;
        this.postfixOp = postfixOp;
        this.prefixOp = prefixOp;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPostfixop() {
        return postfixOp;
    }

    public void setPostfixop(String postfixOp) {
        this.postfixOp = postfixOp;
    }
    public String getPrefixop() {
        return prefixOp;
    }

    public void setPrefixop(String prefixOp) {
        this.prefixOp = prefixOp;
    }

    public alf_InvocationOrAssignementOrDeclarationStatement getAlf_invocationorassignementordeclarationstatement() {
        return alf_invocationorassignementordeclarationstatement;
    }

    public void setAlf_invocationorassignementordeclarationstatement(alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement) {
        this.alf_invocationorassignementordeclarationstatement = alf_invocationorassignementordeclarationstatement;
    }

}