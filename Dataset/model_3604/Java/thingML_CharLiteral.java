





import java.util.List;
import java.util.ArrayList;

public class thingML_CharLiteral extends Literal {

    private String charValue;



    public thingML_CharLiteral(
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