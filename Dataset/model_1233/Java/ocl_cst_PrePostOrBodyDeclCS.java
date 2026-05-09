





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_PrePostOrBodyDeclCS extends CSTNode {

    private String kind;





    private SimpleNameCS simplenamecs;




    private OCLExpressionCS oclexpressioncs;


    public ocl_cst_PrePostOrBodyDeclCS(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public SimpleNameCS getSimplenamecs() {
        return simplenamecs;
    }

    public void setSimplenamecs(SimpleNameCS simplenamecs) {
        this.simplenamecs = simplenamecs;
    }
    public OCLExpressionCS getOclexpressioncs() {
        return oclexpressioncs;
    }

    public void setOclexpressioncs(OCLExpressionCS oclexpressioncs) {
        this.oclexpressioncs = oclexpressioncs;
    }

}