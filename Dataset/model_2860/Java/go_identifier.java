





import java.util.List;
import java.util.ArrayList;

public class go_identifier extends OperandName {

    private String LETTER;
    private String DECIMAL_DIGIT;





    private go_TypeName go_typename;


    public go_identifier(
        String LETTER,        String DECIMAL_DIGIT    ) {
        super(
        );
        this.LETTER = LETTER;
        this.DECIMAL_DIGIT = DECIMAL_DIGIT;
    }


    public String getLetter() {
        return LETTER;
    }

    public void setLetter(String LETTER) {
        this.LETTER = LETTER;
    }
    public String getDecimal_digit() {
        return DECIMAL_DIGIT;
    }

    public void setDecimal_digit(String DECIMAL_DIGIT) {
        this.DECIMAL_DIGIT = DECIMAL_DIGIT;
    }

    public go_TypeName getGo_typename() {
        return go_typename;
    }

    public void setGo_typename(go_TypeName go_typename) {
        this.go_typename = go_typename;
    }

}