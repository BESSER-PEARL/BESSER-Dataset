





import java.util.List;
import java.util.ArrayList;

public class iot2_Statement_If_Then_Else extends Statement {






    private iot2_Block iot2_block;




    private iot2_Block iot2_block;




    private List<iot2_Statement_If_Then_Else_ElseIfPart> iot2_statement_if_then_else_elseifparts;




    private iot2_Expression iot2_expression;


    public iot2_Statement_If_Then_Else(
    ) {
        super(
        );
        this.iot2_statement_if_then_else_elseifparts = new ArrayList<>();
    }

    public iot2_Statement_If_Then_Else(
        ArrayList<iot2_Statement_If_Then_Else_ElseIfPart> iot2_statement_if_then_else_elseifparts    ) {
        this.iot2_statement_if_then_else_elseifparts = iot2_statement_if_then_else_elseifparts;
    }


    public iot2_Block getIot2_block() {
        return iot2_block;
    }

    public void setIot2_block(iot2_Block iot2_block) {
        this.iot2_block = iot2_block;
    }
    public iot2_Block getIot2_block() {
        return iot2_block;
    }

    public void setIot2_block(iot2_Block iot2_block) {
        this.iot2_block = iot2_block;
    }
    public List<iot2_Statement_If_Then_Else_ElseIfPart> getIot2_statement_if_then_else_elseifparts() {
        return iot2_statement_if_then_else_elseifparts;
    }

    public void addIot2_statement_if_then_else_elseifpart(Iot2_statement_if_then_else_elseifpart iot2_statement_if_then_else_elseifpart) {
        this.iot2_statement_if_then_else_elseifparts.add(iot2_statement_if_then_else_elseifpart);
    }
    public iot2_Expression getIot2_expression() {
        return iot2_expression;
    }

    public void setIot2_expression(iot2_Expression iot2_expression) {
        this.iot2_expression = iot2_expression;
    }

}