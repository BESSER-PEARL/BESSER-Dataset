





import java.util.List;
import java.util.ArrayList;

public class sADL_NumberLiteral extends Expression {

    private String value;



    public sADL_NumberLiteral(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}