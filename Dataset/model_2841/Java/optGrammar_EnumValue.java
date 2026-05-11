





import java.util.List;
import java.util.ArrayList;

public class optGrammar_EnumValue  {

    private String name;





    private optGrammar_EnumDefinition optgrammar_enumdefinition;


    public optGrammar_EnumValue(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public optGrammar_EnumDefinition getOptgrammar_enumdefinition() {
        return optgrammar_enumdefinition;
    }

    public void setOptgrammar_enumdefinition(optGrammar_EnumDefinition optgrammar_enumdefinition) {
        this.optgrammar_enumdefinition = optgrammar_enumdefinition;
    }

}