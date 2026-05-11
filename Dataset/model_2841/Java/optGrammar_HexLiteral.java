





import java.util.List;
import java.util.ArrayList;

public class optGrammar_HexLiteral  {

    private String value;





    private optGrammar_NumericLiteral optgrammar_numericliteral;


    public optGrammar_HexLiteral(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public optGrammar_NumericLiteral getOptgrammar_numericliteral() {
        return optgrammar_numericliteral;
    }

    public void setOptgrammar_numericliteral(optGrammar_NumericLiteral optgrammar_numericliteral) {
        this.optgrammar_numericliteral = optgrammar_numericliteral;
    }

}