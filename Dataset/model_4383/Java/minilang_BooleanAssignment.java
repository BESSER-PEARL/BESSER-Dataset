





import java.util.List;
import java.util.ArrayList;

public class minilang_BooleanAssignment extends Statement {






    private minilang_BooleanExpression minilang_booleanexpression;




    private minilang_BooleanVariableRef minilang_booleanvariableref;


    public minilang_BooleanAssignment(
    ) {
        super(
        );
    }



    public minilang_BooleanExpression getMinilang_booleanexpression() {
        return minilang_booleanexpression;
    }

    public void setMinilang_booleanexpression(minilang_BooleanExpression minilang_booleanexpression) {
        this.minilang_booleanexpression = minilang_booleanexpression;
    }
    public minilang_BooleanVariableRef getMinilang_booleanvariableref() {
        return minilang_booleanvariableref;
    }

    public void setMinilang_booleanvariableref(minilang_BooleanVariableRef minilang_booleanvariableref) {
        this.minilang_booleanvariableref = minilang_booleanvariableref;
    }

}