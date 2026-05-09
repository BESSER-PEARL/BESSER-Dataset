





import java.util.List;
import java.util.ArrayList;

public class ast_CharacterLiteral extends Expression {

    private String escapedValue;



    public ast_CharacterLiteral(
        String escapedValue    ) {
        super(
        );
        this.escapedValue = escapedValue;
    }


    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }


}