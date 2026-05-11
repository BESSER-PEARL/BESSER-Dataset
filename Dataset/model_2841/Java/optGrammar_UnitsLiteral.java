





import java.util.List;
import java.util.ArrayList;

public class optGrammar_UnitsLiteral  {

    private String value;





    private optGrammar_UnitTypes optgrammar_unittypes;


    public optGrammar_UnitsLiteral(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public optGrammar_UnitTypes getOptgrammar_unittypes() {
        return optgrammar_unittypes;
    }

    public void setOptgrammar_unittypes(optGrammar_UnitTypes optgrammar_unittypes) {
        this.optgrammar_unittypes = optgrammar_unittypes;
    }

}