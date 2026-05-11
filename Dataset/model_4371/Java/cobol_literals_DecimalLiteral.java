





import java.util.List;
import java.util.ArrayList;

public class cobol_literals_DecimalLiteral extends NumericLiteral {

    private String value;



    public cobol_literals_DecimalLiteral(
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