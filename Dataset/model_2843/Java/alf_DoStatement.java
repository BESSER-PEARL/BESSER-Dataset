





import java.util.List;
import java.util.ArrayList;

public class alf_DoStatement extends Statement {






    private alf_Block alf_block;




    private alf_Expression alf_expression;


    public alf_DoStatement(
    ) {
        super(
        );
    }



    public alf_Block getAlf_block() {
        return alf_block;
    }

    public void setAlf_block(alf_Block alf_block) {
        this.alf_block = alf_block;
    }
    public alf_Expression getAlf_expression() {
        return alf_expression;
    }

    public void setAlf_expression(alf_Expression alf_expression) {
        this.alf_expression = alf_expression;
    }

}