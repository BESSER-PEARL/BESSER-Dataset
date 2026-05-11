





import java.util.List;
import java.util.ArrayList;

public class optGrammar_FunctionDefinition extends DefinitionBody {

    private String name;





    private optGrammar_FunctionCall optgrammar_functioncall;


    public optGrammar_FunctionDefinition(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public optGrammar_FunctionCall getOptgrammar_functioncall() {
        return optgrammar_functioncall;
    }

    public void setOptgrammar_functioncall(optGrammar_FunctionCall optgrammar_functioncall) {
        this.optgrammar_functioncall = optgrammar_functioncall;
    }

}