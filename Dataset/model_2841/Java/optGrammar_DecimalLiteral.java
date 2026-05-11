





import java.util.List;
import java.util.ArrayList;

public class optGrammar_DecimalLiteral  {

    private float value;





    private optGrammar_NumericLiteral optgrammar_numericliteral;


    public optGrammar_DecimalLiteral(
        float value    ) {
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public optGrammar_NumericLiteral getOptgrammar_numericliteral() {
        return optgrammar_numericliteral;
    }

    public void setOptgrammar_numericliteral(optGrammar_NumericLiteral optgrammar_numericliteral) {
        this.optgrammar_numericliteral = optgrammar_numericliteral;
    }

}