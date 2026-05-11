





import java.util.List;
import java.util.ArrayList;

public class optGrammar_FunctionCallArg  {

    private String name;





    private optGrammar_FunctionCallArguments optgrammar_functioncallarguments;




    private optGrammar_Expression optgrammar_expression;


    public optGrammar_FunctionCallArg(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public optGrammar_FunctionCallArguments getOptgrammar_functioncallarguments() {
        return optgrammar_functioncallarguments;
    }

    public void setOptgrammar_functioncallarguments(optGrammar_FunctionCallArguments optgrammar_functioncallarguments) {
        this.optgrammar_functioncallarguments = optgrammar_functioncallarguments;
    }
    public optGrammar_Expression getOptgrammar_expression() {
        return optgrammar_expression;
    }

    public void setOptgrammar_expression(optGrammar_Expression optgrammar_expression) {
        this.optgrammar_expression = optgrammar_expression;
    }

}