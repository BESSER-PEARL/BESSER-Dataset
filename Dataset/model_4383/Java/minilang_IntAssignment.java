





import java.util.List;
import java.util.ArrayList;

public class minilang_IntAssignment extends Statement {






    private minilang_IntVariableRef minilang_intvariableref;




    private minilang_IntExpression minilang_intexpression;


    public minilang_IntAssignment(
    ) {
        super(
        );
    }



    public minilang_IntVariableRef getMinilang_intvariableref() {
        return minilang_intvariableref;
    }

    public void setMinilang_intvariableref(minilang_IntVariableRef minilang_intvariableref) {
        this.minilang_intvariableref = minilang_intvariableref;
    }
    public minilang_IntExpression getMinilang_intexpression() {
        return minilang_intexpression;
    }

    public void setMinilang_intexpression(minilang_IntExpression minilang_intexpression) {
        this.minilang_intexpression = minilang_intexpression;
    }

}