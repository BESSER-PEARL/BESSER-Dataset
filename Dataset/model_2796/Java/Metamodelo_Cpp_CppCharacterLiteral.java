





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppCharacterLiteral extends CppExpression {

    private String charValue;



    public Metamodelo_Cpp_CppCharacterLiteral(
        String charValue    ) {
        super(
        );
        this.charValue = charValue;
    }


    public String getCharvalue() {
        return charValue;
    }

    public void setCharvalue(String charValue) {
        this.charValue = charValue;
    }


}