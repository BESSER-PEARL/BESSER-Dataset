





import java.util.List;
import java.util.ArrayList;

public class optGrammar_versionOperator  {

    private String value;





    private optGrammar_PragmaDirective optgrammar_pragmadirective;


    public optGrammar_versionOperator(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public optGrammar_PragmaDirective getOptgrammar_pragmadirective() {
        return optgrammar_pragmadirective;
    }

    public void setOptgrammar_pragmadirective(optGrammar_PragmaDirective optgrammar_pragmadirective) {
        this.optgrammar_pragmadirective = optgrammar_pragmadirective;
    }

}