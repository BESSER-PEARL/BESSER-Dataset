





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppStringLiteral extends CppExpression {

    private String literalValue;



    public Metamodelo_Cpp_CppStringLiteral(
        String literalValue    ) {
        super(
        );
        this.literalValue = literalValue;
    }


    public String getLiteralvalue() {
        return literalValue;
    }

    public void setLiteralvalue(String literalValue) {
        this.literalValue = literalValue;
    }


}