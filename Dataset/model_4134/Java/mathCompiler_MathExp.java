





import java.util.List;
import java.util.ArrayList;

public class mathCompiler_MathExp  {

    private String line;





    private mathCompiler_Expressions mathcompiler_expressions;


    public mathCompiler_MathExp(
        String line    ) {
        this.line = line;
    }


    public String getLine() {
        return line;
    }

    public void setLine(String line) {
        this.line = line;
    }

    public mathCompiler_Expressions getMathcompiler_expressions() {
        return mathcompiler_expressions;
    }

    public void setMathcompiler_expressions(mathCompiler_Expressions mathcompiler_expressions) {
        this.mathcompiler_expressions = mathcompiler_expressions;
    }

}