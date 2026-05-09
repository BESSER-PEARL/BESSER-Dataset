





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_LocalVariable extends VariableDeclaration {

    private String eq;





    private OclExpression oclexpression;




    private LetExp letexp;


    public gbind_simpleocl_LocalVariable(
        String eq    ) {
        super(
        );
        this.eq = eq;
    }


    public String getEq() {
        return eq;
    }

    public void setEq(String eq) {
        this.eq = eq;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public LetExp getLetexp() {
        return letexp;
    }

    public void setLetexp(LetExp letexp) {
        this.letexp = letexp;
    }

}