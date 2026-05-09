





import java.util.List;
import java.util.ArrayList;

public class JDTAST_EnhancedForStatement extends Statement {






    private JDTAST_Expression jdtast_expression;




    private JDTAST_Statement jdtast_statement;




    private JDTAST_SingleVariableDeclaration jdtast_singlevariabledeclaration;


    public JDTAST_EnhancedForStatement(
    ) {
        super(
        );
    }



    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }
    public JDTAST_Statement getJdtast_statement() {
        return jdtast_statement;
    }

    public void setJdtast_statement(JDTAST_Statement jdtast_statement) {
        this.jdtast_statement = jdtast_statement;
    }
    public JDTAST_SingleVariableDeclaration getJdtast_singlevariabledeclaration() {
        return jdtast_singlevariabledeclaration;
    }

    public void setJdtast_singlevariabledeclaration(JDTAST_SingleVariableDeclaration jdtast_singlevariabledeclaration) {
        this.jdtast_singlevariabledeclaration = jdtast_singlevariabledeclaration;
    }

}