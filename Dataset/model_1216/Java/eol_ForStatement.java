





import java.util.List;
import java.util.ArrayList;

public class eol_ForStatement extends Statement {






    private eol_Block eol_block;




    private eol_Expression eol_expression;


    public eol_ForStatement(
    ) {
        super(
        );
    }



    public eol_Block getEol_block() {
        return eol_block;
    }

    public void setEol_block(eol_Block eol_block) {
        this.eol_block = eol_block;
    }
    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }

}