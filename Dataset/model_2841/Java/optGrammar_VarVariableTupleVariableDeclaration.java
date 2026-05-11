





import java.util.List;
import java.util.ArrayList;

public class optGrammar_VarVariableTupleVariableDeclaration extends SimpleStatement, SimpleStatement2 {

    private boolean semicolon;



    public optGrammar_VarVariableTupleVariableDeclaration(
        boolean semicolon    ) {
        super(
        );
        this.semicolon = semicolon;
    }


    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }


}