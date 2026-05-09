





import java.util.List;
import java.util.ArrayList;

public class simpleocl_LocalVariable extends VariableDeclaration {

    private String eq;





    private simpleocl_LetExp simpleocl_letexp;




    private simpleocl_OclExpression simpleocl_oclexpression;




    private simpleocl_LetExp simpleocl_letexp;




    private simpleocl_OclExpression simpleocl_oclexpression;


    public simpleocl_LocalVariable(
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

    public simpleocl_LetExp getSimpleocl_letexp() {
        return simpleocl_letexp;
    }

    public void setSimpleocl_letexp(simpleocl_LetExp simpleocl_letexp) {
        this.simpleocl_letexp = simpleocl_letexp;
    }
    public simpleocl_OclExpression getSimpleocl_oclexpression() {
        return simpleocl_oclexpression;
    }

    public void setSimpleocl_oclexpression(simpleocl_OclExpression simpleocl_oclexpression) {
        this.simpleocl_oclexpression = simpleocl_oclexpression;
    }
    public simpleocl_LetExp getSimpleocl_letexp() {
        return simpleocl_letexp;
    }

    public void setSimpleocl_letexp(simpleocl_LetExp simpleocl_letexp) {
        this.simpleocl_letexp = simpleocl_letexp;
    }
    public simpleocl_OclExpression getSimpleocl_oclexpression() {
        return simpleocl_oclexpression;
    }

    public void setSimpleocl_oclexpression(simpleocl_OclExpression simpleocl_oclexpression) {
        this.simpleocl_oclexpression = simpleocl_oclexpression;
    }

}