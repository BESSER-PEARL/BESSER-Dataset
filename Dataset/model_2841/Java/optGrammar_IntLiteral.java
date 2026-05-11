





import java.util.List;
import java.util.ArrayList;

public class optGrammar_IntLiteral  {

    private int value;





    private optGrammar_NumericLiteral optgrammar_numericliteral;


    public optGrammar_IntLiteral(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public optGrammar_NumericLiteral getOptgrammar_numericliteral() {
        return optgrammar_numericliteral;
    }

    public void setOptgrammar_numericliteral(optGrammar_NumericLiteral optgrammar_numericliteral) {
        this.optgrammar_numericliteral = optgrammar_numericliteral;
    }

}