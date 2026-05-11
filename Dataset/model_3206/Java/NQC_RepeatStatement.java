





import java.util.List;
import java.util.ArrayList;

public class NQC_RepeatStatement extends ControlStructure {






    private NQC_Expression nqc_expression;




    private NQC_Statement nqc_statement;


    public NQC_RepeatStatement(
    ) {
        super(
        );
    }



    public NQC_Expression getNqc_expression() {
        return nqc_expression;
    }

    public void setNqc_expression(NQC_Expression nqc_expression) {
        this.nqc_expression = nqc_expression;
    }
    public NQC_Statement getNqc_statement() {
        return nqc_statement;
    }

    public void setNqc_statement(NQC_Statement nqc_statement) {
        this.nqc_statement = nqc_statement;
    }

}