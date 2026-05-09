





import java.util.List;
import java.util.ArrayList;

public class JDTAST_LabeledStatement extends Statement {






    private JDTAST_Statement jdtast_statement;




    private JDTAST_SimpleName jdtast_simplename;


    public JDTAST_LabeledStatement(
    ) {
        super(
        );
    }



    public JDTAST_Statement getJdtast_statement() {
        return jdtast_statement;
    }

    public void setJdtast_statement(JDTAST_Statement jdtast_statement) {
        this.jdtast_statement = jdtast_statement;
    }
    public JDTAST_SimpleName getJdtast_simplename() {
        return jdtast_simplename;
    }

    public void setJdtast_simplename(JDTAST_SimpleName jdtast_simplename) {
        this.jdtast_simplename = jdtast_simplename;
    }

}